# Dataset Documentation
**Status: NOT YET SELECTED OR LICENSE-VERIFIED.** No dataset was supplied.
Recommended classes: butterfly, cat, dog, elephant, horse.
Before training, record dataset name, original URL, provider/author, download
date, license text, academic-use permissions, attribution requirements and
actual per-class image counts. Place images in `dataset/raw/<class>/`.
The preparation script validates supported image files, reports unreadable
images and exact SHA-256 duplicates, and creates stratified 70/15/15 splits.
It cannot detect all near-duplicates or infer source groups without metadata.
Never invent image counts or claim a license without checking the provider.
