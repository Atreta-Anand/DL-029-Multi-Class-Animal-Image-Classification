# DL-029 — AnimalVision AI
Invertis University, Bareilly | B.Tech CSE | Semester V | Group BTech_DL_051
Mentor: Pradeep Singh

A multi-class animal image classification project with a custom CNN and
MobileNetV2 transfer-learning pipeline. Recommended classes: butterfly, cat,
dog, elephant and horse.

## Honest status
Source and documentation: CREATED. Real dataset/license: NOT YET VERIFIED.
Real model training and test metrics: NOT YET EXECUTED. No model artifacts or
animal results are fabricated. Streamlit source is included; setup/run is
deferred. GitHub and deployment are out of scope for this phase.

## Setup (Windows PowerShell)
Python 3.10–3.12 recommended:
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```
Dataset instructions: see reports/DATASET_DOCUMENTATION.md. Place class folders
under dataset/raw/ and run:
```powershell
python eda.py
python main.py --prepare
python train_model.py --architecture custom_cnn --epochs 15
python train_model.py --architecture mobilenetv2 --epochs 15
python evaluate_model.py --model models/custom_cnn.keras
pytest -q
```
For MobileNetV2 pretrained weights, network access may be needed. `--no-pretrained`
uses random initialization and must not be called pretrained transfer learning.
