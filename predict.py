from pathlib import Path
import json, numpy as np
from config import MODEL_DIR
from preprocessing import prepare_batch

def predict_image(image,model_path=None):
    import tensorflow as tf
    path=Path(model_path or MODEL_DIR/"mobilenetv2.keras")
    if not path.is_file(): raise FileNotFoundError(f"Trained model missing: {path}")
    meta_path=path.with_name(path.stem+"_metadata.json")
    if not meta_path.is_file(): raise FileNotFoundError(f"Metadata missing: {meta_path}")
    meta=json.loads(meta_path.read_text()); classes=meta["classes"]; arch=meta["architecture"]
    model=tf.keras.models.load_model(path)
    scores=model.predict(prepare_batch(image,tuple(meta["image_size"]),arch),verbose=0)[0]
    idx=int(np.argmax(scores))
    return {"predicted_class":classes[idx],"confidence":float(scores[idx]),
        "probabilities":{c:float(scores[i]) for i,c in enumerate(classes)}}
