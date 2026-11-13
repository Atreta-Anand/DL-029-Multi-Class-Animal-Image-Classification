DL-029 Animal Classification - starter image pack

This pack includes a one-command downloader and the five required class folders.
It downloads one CC0 1.0 example image for each class from Wikimedia Commons and writes ATTRIBUTION.csv.

IMPORTANT: 5 images total (1 per class) are ONLY for testing folder paths and the download process.
They are not enough for model training or final submission.
For a credible project, aim for at least 100-200 distinct, correctly licensed images per class (500-1,000 total), subject to your project requirements. Keep source/license records for every image.

HOW TO USE
1. Extract this ZIP into your project root: C:\DL-029-Multi-Class-Animal-Image-Classification
2. Open VS Code in that project folder.
3. Open Terminal (Terminal > New Terminal).
4. Ensure the terminal is in the project root and run:
   python .\animal_dataset_starter\download_starter_images.py
5. The five images will be placed in your existing dataset/raw/<class>/ folders and ATTRIBUTION.csv will be created in the project root.

The direct download script requires an internet connection. If Wikimedia blocks a request, open the corresponding source_page in ATTRIBUTION.csv and download the original file manually.
