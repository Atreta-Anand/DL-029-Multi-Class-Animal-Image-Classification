from pathlib import Path
import time, numpy as np
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
from config import SPLIT_ROOT,MODEL_DIR,OUTPUT_DIR,IMAGE_SIZE
from utils import save_json

def evaluate(model_path):
    import tensorflow as tf
    model_path=Path(model_path); classes=sorted(p.name for p in (SPLIT_ROOT/"test").iterdir() if p.is_dir())
    ds=tf.keras.utils.image_dataset_from_directory(SPLIT_ROOT/"test",class_names=classes,image_size=IMAGE_SIZE,
        batch_size=16,shuffle=False)
    y=np.concatenate([labels.numpy() for _,labels in ds]); model=tf.keras.models.load_model(model_path)
    start=time.perf_counter(); probs=model.predict(ds,verbose=0); elapsed=time.perf_counter()-start; pred=probs.argmax(1)
    report=classification_report(y,pred,target_names=classes,output_dict=True,zero_division=0)
    result={"accuracy":float(accuracy_score(y,pred)),"macro_precision":report["macro avg"]["precision"],
        "macro_recall":report["macro avg"]["recall"],"macro_f1":report["macro avg"]["f1-score"],
        "test_images":int(len(y)),"prediction_seconds_total":elapsed,"classes":classes,
        "classification_report":report,"confusion_matrix":confusion_matrix(y,pred).tolist()}
    out=OUTPUT_DIR/"evaluation"; out.mkdir(parents=True,exist_ok=True); save_json(result,out/f"{model_path.stem}_metrics.json")
    save_json({"y_true":y.tolist(),"y_pred":pred.tolist(),"probabilities":probs.tolist()},out/f"{model_path.stem}_predictions.json")
    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from sklearn.metrics import ConfusionMatrixDisplay
    fig,ax=plt.subplots(figsize=(7,6)); ConfusionMatrixDisplay(confusion_matrix(y,pred),display_labels=classes).plot(ax=ax,colorbar=False)
    fig.tight_layout(); fig.savefig(out/f"{model_path.stem}_confusion_matrix.png",dpi=150); plt.close(fig)
    return result
if __name__=="__main__":
    import argparse,json
    p=argparse.ArgumentParser(); p.add_argument("--model",default=str(MODEL_DIR/"mobilenetv2.keras"))
    print(json.dumps(evaluate(p.parse_args().model),indent=2))
