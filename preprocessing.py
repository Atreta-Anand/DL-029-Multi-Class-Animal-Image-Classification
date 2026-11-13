from pathlib import Path
from PIL import Image
import numpy as np

def load_rgb_image(source, image_size=(224,224)):
    if isinstance(source, Image.Image):
        im=source.copy()
    elif isinstance(source,(str,Path)):
        with Image.open(source) as f:
            f.load(); im=f.copy()
    else:
        raise TypeError("Expected image path or PIL image")
    return im.convert("RGB").resize(tuple(image_size),Image.Resampling.BILINEAR)

def image_to_array(source,image_size=(224,224)):
    return np.asarray(load_rgb_image(source,image_size),dtype=np.float32)/255.0


def prepare_batch(source, image_size=(224,224), architecture="custom_cnn"):
    arr = np.asarray(
        load_rgb_image(source, image_size),
        dtype=np.float32
    )[None, ...]
    return arr


