from pathlib import Path
import os
ROOT=Path(__file__).resolve().parent
PROJECT_ID = "DL-029-Multi-Class-Animal-Image-Classification"
DATASET_ROOT=Path(os.getenv("DL029_DATASET_DIR", ROOT/"dataset/raw"))
SPLIT_ROOT=ROOT/"dataset/splits"
MODEL_DIR=ROOT/"models"
OUTPUT_DIR=ROOT/"outputs"
IMAGE_SIZE=(224,224)
CLASS_NAMES=["butterfly","cat","dog","elephant","horse"]
BATCH_SIZE=16
EPOCHS=15
LEARNING_RATE=1e-3
SEED=42
