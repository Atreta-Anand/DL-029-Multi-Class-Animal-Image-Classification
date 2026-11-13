# System Architecture
Data layer: class folders in dataset/raw. Validation layer: readable images,
formats, exact hashes and class folders. Preparation: reproducible split and
resize. Learning: custom CNN or MobileNetV2. Evaluation: class metrics and
confusion matrix on held-out test. Persistence: Keras model and JSON metadata.
Presentation: Streamlit app source, to be configured later.
