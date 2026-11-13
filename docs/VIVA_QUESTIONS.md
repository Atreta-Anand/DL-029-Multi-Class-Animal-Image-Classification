# Viva Questions and Answers

### 1. What is deep learning?
Neural networks that learn layered representations from data.

### 2. What is computer vision?
The field of extracting information from images and videos.

### 3. What is image classification?
Assigning an image to one predefined label.

### 4. What is multi-class classification?
Choosing one class from more than two possible classes.

### 5. What is a CNN?
A neural network using convolution to learn spatial features.

### 6. What is transfer learning?
Reusing learned model weights for a related task.

### 7. What is convolution?
Applying a learnable filter across an input.

### 8. What is a kernel?
A small learnable filter matrix.

### 9. What is a feature map?
The activation output of a convolution.

### 10. What is ReLU?
The activation max(0,x).

### 11. What is MaxPooling?
Downsampling by taking local maximum values.

### 12. What is Batch Normalization?
Normalizing intermediate activations to help training.

### 13. What is Dropout?
Randomly disabling units during training as regularization.

### 14. What is Global Average Pooling?
Averaging each feature map over its spatial dimensions.

### 15. What is Softmax?
Converting logits into scores that sum to one.

### 16. What is cross-entropy loss?
A loss measuring mismatch between target labels and predicted distribution.

### 17. What is backpropagation?
Computing gradients through the network using the chain rule.

### 18. What is MobileNetV2?
An efficient CNN with inverted residual blocks and linear bottlenecks.

### 19. What are pretrained weights?
Weights learned previously on another dataset.

### 20. What is ImageNet?
A large image dataset commonly used for model pretraining.

### 21. What does freezing mean?
Keeping selected layer weights unchanged during training.

### 22. What is fine-tuning?
Training some pretrained layers with a small learning rate.

### 23. Why use transfer learning?
It can reuse useful visual features and reduce data needs.

### 24. What is RGB?
A three-channel red, green and blue color representation.

### 25. Why resize images?
To provide consistent input dimensions to a model.

### 26. What is normalization?
Scaling input values to a suitable numeric range.

### 27. What is augmentation?
Applying label-preserving transformations to training samples.

### 28. Why not augment test data?
Test data should represent the untouched evaluation distribution.

### 29. What is an epoch?
One full pass through the training data.

### 30. What is batch size?
Number of samples processed per gradient update.

### 31. What is learning rate?
The scale of an optimizer's parameter updates.

### 32. What is an optimizer?
An algorithm that updates model parameters to reduce loss.

### 33. What is Adam?
An adaptive optimizer using moving averages of gradients and squared gradients.

### 34. What is EarlyStopping?
Stopping when a monitored validation metric ceases improving.

### 35. What is overfitting?
Good training performance but poor generalization.

### 36. What is underfitting?
A model failing to learn the underlying patterns.

### 37. What is accuracy?
Correct predictions divided by all predictions.

### 38. What is precision?
True positives divided by predicted positives.

### 39. What is recall?
True positives divided by actual positives.

### 40. What is F1-score?
The harmonic mean of precision and recall.

### 41. What is macro averaging?
Unweighted average of per-class metric values.

### 42. What is a confusion matrix?
A table of true versus predicted class counts.

### 43. Why per-class metrics?
They expose weak classes hidden by overall accuracy.

### 44. Why save a model?
To reuse learned weights for inference without retraining.

### 45. Why Streamlit?
It makes interactive Python web apps with little frontend code.

### 46. What are project limitations?
Predictions are limited to trained labels and depend on data quality and conditions.