# DL-029 Explanation in Hinglish
Project ka goal animal image ko selected classes me classify karna hai.
Recommended classes Cat, Dog, Horse, Elephant aur Butterfly hain. Dataset
download karne se pehle license verify karna zaroori hai.

**RGB:** Red, Green, Blue channels. **Resize:** sab images ko 224×224 banana.
**Normalization:** pixel values ko model-friendly range me scale karna.
**Augmentation:** training images par flip, rotation, zoom, translation aur
contrast variation; validation/test ko augment nahi karte.

**CNN:** image patterns learn karne wala neural network. **Convolution:** filter
image par slide karke features nikalta hai. **Kernel/filter:** learnable small
matrix. **Feature map:** convolution output. **ReLU:** negative values ko zero.
**MaxPooling:** spatial dimensions kam karta hai. **Dropout:** overfitting
reduce karne ke liye training me units randomly off karta hai. **Softmax:**
class scores ko normalized distribution banata hai.

**MobileNetV2:** efficient pretrained CNN. **Transfer Learning:** pehle se
learned weights reuse karna. **Freeze:** layer weights update na karna.
**Fine-tuning:** selected layers ko low learning rate se train karna.

**Epoch:** training data ka ek full pass. **Batch size:** ek update se pehle
samples ki sankhya. **Learning rate:** update step size. **Adam:** optimizer.
**EarlyStopping:** validation improvement rukne par training rokna.

**Accuracy:** total correct ratio. **Precision:** predicted positives me
correct fraction. **Recall:** actual positives me found fraction. **F1:** dono
ka harmonic mean. **Macro average:** har class ko equal weight. **Confusion
matrix:** actual vs predicted class counts.

Prediction flow: upload → RGB → resize → same normalization → model inference →
top class and scores. Current build me source code hai; real dataset/training
results abhi available nahi.
