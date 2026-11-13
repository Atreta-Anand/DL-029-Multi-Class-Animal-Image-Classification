from pathlib import Path
import json, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image
from config import DATASET_ROOT,OUTPUT_DIR,CLASS_NAMES
from dataset_loader import inspect_dataset

def run_eda(dataset_root=DATASET_ROOT,output_dir=OUTPUT_DIR/"eda"):
    output_dir=Path(output_dir); output_dir.mkdir(parents=True,exist_ok=True)
    report=inspect_dataset(dataset_root,CLASS_NAMES)
    (output_dir/"dataset_inspection.json").write_text(json.dumps(report,indent=2))
    fig,ax=plt.subplots(figsize=(9,5)); ax.bar(report["class_counts"].keys(),report["class_counts"].values())
    ax.set(xlabel="Animal class",ylabel="Image count",title="Dataset class distribution")
    fig.tight_layout(); fig.savefig(output_dir/"class_distribution.png",dpi=150); plt.close(fig)
    paths=report["valid_images"][:15]
    if paths:
        cols=5; rows=(len(paths)+cols-1)//cols; fig,axs=plt.subplots(rows,cols,figsize=(12,3*rows))
        axs=list(axs.flat) if hasattr(axs,"flat") else [axs]
        for ax,p in zip(axs,paths):
            with Image.open(p) as im: ax.imshow(im.convert("RGB"))
            ax.set_title(Path(p).parent.name); ax.axis("off")
        for ax in axs[len(paths):]: ax.axis("off")
        fig.tight_layout(); fig.savefig(output_dir/"sample_gallery.png",dpi=150); plt.close(fig)
    return report
if __name__=="__main__": print(json.dumps(run_eda(),indent=2))
