from PIL import Image
import numpy as np, pytest
from preprocessing import load_rgb_image,image_to_array,prepare_batch

def test_rgb_resize():
    im=Image.new("RGBA",(30,10),(255,0,0,100))
    out=load_rgb_image(im,(224,224))
    assert out.mode=="RGB" and out.size==(224,224)
    a=image_to_array(im)
    assert a.shape==(224,224,3) and a.dtype==np.float32
    assert 0<=a.min()<=a.max()<=1

def test_batches():
    im=Image.new("RGB",(10,10),"white")
    assert prepare_batch(im,(32,32),"custom_cnn").shape==(1,32,32,3)
    assert np.allclose(prepare_batch(im,(32,32),"mobilenetv2"),1.0)

def test_bad_input():
    with pytest.raises(TypeError): load_rgb_image(7)
