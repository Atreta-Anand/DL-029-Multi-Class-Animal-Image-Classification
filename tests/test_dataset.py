from PIL import Image
import pytest
from dataset_loader import inspect_dataset,create_splits

def make(root,n=20):
    for c in ["cat","dog","horse","elephant","butterfly"]:
        d=root/c; d.mkdir(parents=True)
        for i in range(n): Image.new("RGB",(24+i,20),(i*5,20,30)).save(d/f"{i}.jpg")

def test_inspection(tmp_path):
    make(tmp_path); r=inspect_dataset(tmp_path)
    assert r["class_counts"]["cat"]==20 and len(r["valid_images"])==100

def test_missing_class(tmp_path):
    (tmp_path/"cat").mkdir()
    with pytest.raises(FileNotFoundError): inspect_dataset(tmp_path)

def test_split(tmp_path):
    raw=tmp_path/"raw"; raw.mkdir(); make(raw)
    r=create_splits(raw,tmp_path/"split")
    assert r["train"]+r["validation"]+r["test"]==100
