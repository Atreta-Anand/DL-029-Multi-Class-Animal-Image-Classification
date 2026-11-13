import json, random, os
from pathlib import Path
def set_seed(seed=42):
    random.seed(seed); os.environ["PYTHONHASHSEED"]=str(seed)
    try:
        import numpy as np; np.random.seed(seed)
    except ImportError: pass
    try:
        import tensorflow as tf; tf.random.set_seed(seed)
    except ImportError: pass
def save_json(data,path):
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(data,indent=2,default=str),encoding="utf-8")
