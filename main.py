from config import *
from dataset_loader import inspect_dataset,create_splits
from eda import run_eda
from train_model import train
from utils import save_json
import argparse

def main():
    p=argparse.ArgumentParser(); p.add_argument("--prepare",action="store_true"); p.add_argument("--train",action="store_true")
    p.add_argument("--architecture",choices=["custom_cnn","mobilenetv2"],default="mobilenetv2")
    p.add_argument("--epochs",type=int,default=EPOCHS); a=p.parse_args()
    if a.prepare:
        report=inspect_dataset(DATASET_ROOT,CLASS_NAMES); save_json(report,OUTPUT_DIR/"dataset_inspection.json")
        print("Split:",create_splits(DATASET_ROOT,SPLIT_ROOT,CLASS_NAMES)); run_eda()
    if a.train: print("Model:",train(a.architecture,a.epochs))
    if not a.prepare and not a.train: p.print_help()
if __name__=="__main__": main()
