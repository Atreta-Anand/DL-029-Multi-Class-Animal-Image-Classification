# Invertis University — DL-029 Project Report
## Multi-Class Animal Image Classification
**Department:** CSE | **Programme:** B.Tech | **Semester:** V | **Section:** E  
**Group:** BTech_DL_051 | **Mentor:** Pradeep Singh  
**Student details:** [Fill using verified official details]

### Index
Introduction; Problem Statement; Objectives; Literature Review; Dataset;
Methodology; Architecture; Implementation; Results; Limitations; Future Scope;
Conclusion; References.

### Introduction and problem
This project investigates image classification among four to six selected
animal categories using a CNN and MobileNetV2 transfer learning.

### Objectives
Prepare a licensed dataset, preprocess images consistently, train models,
evaluate class-wise performance, analyze confusion, and provide an image
upload prediction interface.

### Dataset
Not yet selected or license-verified. Recommended labels are cat, dog, horse,
elephant and butterfly. Complete DATASET_DOCUMENTATION.md before experiments.

### Methodology
Validate images, convert to RGB, resize to 224×224, create stratified 70/15/15
splits, and apply augmentation only to training data. Evaluate once on the
untouched test partition.

### Architecture
Image folders → validation → split → preprocessing/augmentation → CNN or
MobileNetV2 → model persistence → test metrics → prediction interface.

### Implementation
See Python modules in the project root and SYSTEM_ARCHITECTURE.md.

### Results and discussion
Not yet executed. Insert genuine training curves, classification report,
confusion matrix, per-class analysis and different-background tests after
running on a licensed dataset.

### Future scope
Source-aware splitting, perceptual duplicate detection, calibrated confidence,
external validation, controlled fine-tuning and deployment.

### Conclusion
This package is the implementation foundation. Research conclusions must wait
for real data inspection, training and untouched-test evaluation.

### References
Sandler et al. (2018), MobileNetV2: Inverted Residuals and Linear Bottlenecks,
CVPR. https://arxiv.org/abs/1801.04381  
TensorFlow: https://www.tensorflow.org/  
Keras: https://keras.io/  
scikit-learn: https://scikit-learn.org/stable/
