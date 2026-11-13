from pathlib import Path
from PIL import Image, UnidentifiedImageError
from sklearn.model_selection import train_test_split
import hashlib, shutil
EXT={".jpg",".jpeg",".png",".bmp",".webp"}

def inspect_dataset(root,class_names=None):
    root=Path(root); classes=class_names or ["butterfly","cat","dog","elephant","horse"]
    if not root.is_dir(): raise FileNotFoundError(root)
    out={"class_counts":{},"valid_images":[],"invalid_images":[],"duplicates":[],"dimensions":{},"formats":{}}
    hashes={}
    for cls in classes:
        folder=root/cls
        if not folder.is_dir(): raise FileNotFoundError(f"Missing class folder: {folder}")
        count=0
        for p in sorted(folder.rglob("*")):
            if not p.is_file(): continue
            if p.suffix.lower() not in EXT:
                out["invalid_images"].append({"path":str(p),"reason":"unsupported extension"}); continue
            try:
                with Image.open(p) as im: im.verify()
                with Image.open(p) as im: w,h=im.size; fmt=im.format or p.suffix[1:]
                digest=hashlib.sha256(p.read_bytes()).hexdigest()
                if digest in hashes: out["duplicates"].append({"path":str(p),"duplicate_of":hashes[digest]})
                else: hashes[digest]=str(p)
                out["valid_images"].append(str(p)); out["dimensions"][f"{w}x{h}"]=out["dimensions"].get(f"{w}x{h}",0)+1
                out["formats"][fmt]=out["formats"].get(fmt,0)+1; count+=1
            except (OSError,ValueError,UnidentifiedImageError) as e:
                out["invalid_images"].append({"path":str(p),"reason":str(e)})
        out["class_counts"][cls]=count
    return out

def create_splits(root,out_root,class_names=None,val_fraction=.15,test_fraction=.15,seed=42):
    root=Path(root); out_root=Path(out_root)
    classes=class_names or ["butterfly","cat","dog","elephant","horse"]
    paths=[]; labels=[]
    for cls in classes:
        items=[p for p in (root/cls).rglob("*") if p.is_file() and p.suffix.lower() in EXT]
        if len(items)<3: raise ValueError(f"{cls}: need >=3 images, found {len(items)}")
        paths += [str(p) for p in items]; labels += [cls]*len(items)
    tr,tmp,ytr,ytmp=train_test_split(paths,labels,test_size=val_fraction+test_fraction,random_state=seed,stratify=labels)
    va,te,yva,yte=train_test_split(tmp,ytmp,test_size=test_fraction/(val_fraction+test_fraction),random_state=seed,stratify=ytmp)
    for split,ps,ys in [("train",tr,ytr),("validation",va,yva),("test",te,yte)]:
        for src,cls in zip(ps,ys):
            dest=out_root/split/cls; dest.mkdir(parents=True,exist_ok=True); shutil.copy2(src,dest/Path(src).name)
    return {"train":len(tr),"validation":len(va),"test":len(te),"seed":seed}
