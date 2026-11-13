# Workflow
Licensed dataset → class validation → corruption/duplicate audit → stratified
train/validation/test split → RGB resize → training-only augmentation → CNN or
MobileNetV2 → validation-based selection → untouched test evaluation → saved
model/metrics → AnimalVision AI.
