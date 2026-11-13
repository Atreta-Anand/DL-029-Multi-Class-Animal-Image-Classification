
import json
from pathlib import Path

import streamlit as st
import pandas as pd
from PIL import Image

from config import MODEL_DIR, OUTPUT_DIR, PROJECT_ID
from predict import predict_image


st.set_page_config(
    page_title="AnimalVision AI",
    page_icon="🐾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM DESIGN ----------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #f4f7fb;
}

[data-testid="stSidebar"] {
    background: #101b35;
}

[data-testid="stSidebar"] * {
    color: #ffffff !important;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label {
    padding: 9px 12px;
    border-radius: 9px;
}

.main-title {
    font-size: 38px;
    font-weight: 800;
    color: #14213d;
    letter-spacing: -1.5px;
}

.subtitle {
    color: #75819a;
    font-size: 15px;
    margin-bottom: 25px;
}

.hero {
    background: linear-gradient(120deg, #14213d, #2457a7);
    padding: 30px;
    border-radius: 18px;
    color: white;
    margin-bottom: 25px;
}

.hero h2 {
    color: white;
    font-size: 28px;
}

.hero p {
    color: #dce7ff;
    font-size: 15px;
}

.section-title {
    color: #14213d;
    font-size: 23px;
    font-weight: 700;
    margin-top: 20px;
}

.metric-card {
    background: white;
    border: 1px solid #e5eaf2;
    border-radius: 14px;
    padding: 20px;
    min-height: 115px;
    box-shadow: 0 3px 12px rgba(20,33,61,0.04);
}

.metric-label {
    color: #7a879c;
    font-size: 13px;
    font-weight: 600;
}

.metric-value {
    color: #173d7a;
    font-size: 27px;
    font-weight: 800;
    margin-top: 8px;
}

.info-card {
    background: white;
    border: 1px solid #e5eaf2;
    padding: 22px;
    border-radius: 14px;
    margin-bottom: 14px;
}

.result-card {
    background: #e8f8f0;
    border: 1px solid #bcebd2;
    padding: 22px;
    border-radius: 14px;
    color: #087443;
    margin: 15px 0;
}

.stButton > button {
    background: #2457a7;
    color: white;
    border: none;
    border-radius: 9px;
    padding: 10px 25px;
    font-weight: 600;
}

.stButton > button:hover {
    background: #173d7a;
    color: white;
}

div[data-testid="stFileUploader"] {
    background: white;
    border: 2px dashed #a9bddc;
    border-radius: 14px;
    padding: 15px;
}

hr {
    border-color: #e1e7f0;
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ----------------

with st.sidebar:
    st.markdown("# 🐾 AnimalVision")
    st.caption("AI ANIMAL CLASSIFICATION")
    st.markdown("---")

    page = st.radio(
        "MAIN MENU",
        [
            "Home",
            "Image Prediction",
            "Model Performance",
            "Dataset Explorer",
            "Model Information",
            "Project Information"
        ]
    )

    st.markdown("---")
    st.caption("DL-029 | B.Tech CSE")
    st.caption("Powered by MobileNetV2")


# ---------------- HEADER ----------------

st.markdown(
    '<div class="main-title">🐾 AnimalVision AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Multi-Class Animal Image Classification System</div>',
    unsafe_allow_html=True
)


# ---------------- HOME ----------------

if page == "Home":

    st.markdown("""
    <div class="hero">
        <h2>Welcome to AnimalVision AI</h2>
        <p>
        An intelligent computer vision application that identifies
        animals from uploaded images using deep learning and MobileNetV2.
        </p>
        <b>Smart Vision • Deep Learning • Image Recognition</b>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">Project Overview</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    for col, label, value in [
        (c1, "ANIMAL CLASSES", "05"),
        (c2, "MODEL ARCHITECTURE", "MobileNetV2"),
        (c3, "APPLICATION", "Streamlit AI")
    ]:
        with col:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">{label}</div>
                <div class="metric-value">{value}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">Supported Animal Classes</div>',
        unsafe_allow_html=True
    )

    animals = st.columns(5)

    for col, emoji, name in zip(
        animals,
        ["🦋", "🐱", "🐶", "🐘", "🐎"],
        ["Butterfly", "Cat", "Dog", "Elephant", "Horse"]
    ):
        with col:
            st.markdown(f"""
            <div class="info-card" style="text-align:center">
                <div style="font-size:35px">{emoji}</div>
                <b>{name}</b>
            </div>
            """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">Project Workflow</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="info-card">
    <b>01. Dataset</b> → Collect animal images<br><br>
    <b>02. Preprocessing</b> → Resize and normalize images<br><br>
    <b>03. Deep Learning</b> → MobileNetV2 feature extraction<br><br>
    <b>04. Evaluation</b> → Accuracy and classification metrics<br><br>
    <b>05. Prediction</b> → Identify the uploaded animal
    </div>
    """, unsafe_allow_html=True)


# ---------------- IMAGE PREDICTION ----------------

elif page == "Image Prediction":

    st.markdown(
        '<div class="section-title">Image Recognition</div>',
        unsafe_allow_html=True
    )

    st.write("Upload an animal image and let AI identify it.")

    upload = st.file_uploader(
        "Choose an animal image",
        type=["jpg", "jpeg", "png"]
    )

    if upload:

        try:
            image = Image.open(upload).convert("RGB")

            left, right = st.columns([1, 1])

            with left:
                st.image(
                    image,
                    caption="Uploaded Animal Image",
                    use_container_width=True
                )

            with right:
                st.markdown("""
                <div class="info-card">
                    <h3>Image Details</h3>
                    <p>Image uploaded successfully.</p>
                    <p>Format: JPG / JPEG / PNG</p>
                    <p>Model: MobileNetV2</p>
                </div>
                """, unsafe_allow_html=True)

                if st.button("🔍 Analyze Image", use_container_width=True):

                    with st.spinner("AI is analyzing your image..."):

                        result = predict_image(
                            image,
                            MODEL_DIR / "mobilenetv2.keras"
                        )

                    st.session_state["prediction_result"] = result

            if "prediction_result" in st.session_state:

                result = st.session_state["prediction_result"]

                st.markdown("---")
                st.markdown("### 🎯 Prediction Result")

                st.markdown(f"""
                <div class="result-card">
                    <div style="font-size:14px">PREDICTED ANIMAL</div>
                    <div style="font-size:32px;font-weight:800">
                        {result['predicted_class'].title()}
                    </div>
                    <div style="font-size:19px">
                        Confidence: {result['confidence']:.1%}
                    </div>
                </div>
                """, unsafe_allow_html=True)

                st.markdown("### Prediction Probabilities")

                st.bar_chart(
                    pd.Series(result["probabilities"])
                    .sort_values(ascending=False)
                )

        except Exception as e:
            st.error(f"Prediction Error: {e}")


# ---------------- MODEL PERFORMANCE ----------------

elif page == "Model Performance":

    st.markdown(
        '<div class="section-title">Model Performance Analytics</div>',
        unsafe_allow_html=True
    )

    folder = OUTPUT_DIR / "evaluation"
    metrics_file = folder / "mobilenetv2_metrics.json"

    if metrics_file.exists():

        d = json.loads(metrics_file.read_text())

        cols = st.columns(4)

        for col, key, label in zip(
            cols,
            ["accuracy", "macro_precision", "macro_recall", "macro_f1"],
            ["Accuracy", "Macro Precision", "Macro Recall", "Macro F1"]
        ):

            with col:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-label">{label.upper()}</div>
                    <div class="metric-value">{d[key]:.3f}</div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("### Classification Report")

        st.dataframe(
            pd.DataFrame(d["classification_report"]).T,
            use_container_width=True
        )

        pic = folder / "mobilenetv2_confusion_matrix.png"

        if pic.exists():
            st.markdown("### Confusion Matrix")
            st.image(str(pic), use_container_width=True)

    else:
        st.info("MobileNetV2 evaluation metrics are not available yet.")


# ---------------- DATASET EXPLORER ----------------

elif page == "Dataset Explorer":

    st.markdown(
        '<div class="section-title">Dataset Analytics</div>',
        unsafe_allow_html=True
    )

    f = OUTPUT_DIR / "eda" / "dataset_inspection.json"

    if f.exists():

        d = json.loads(f.read_text())

        c1, c2 = st.columns(2)

        with c1:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">VALID IMAGES</div>
                <div class="metric-value">{len(d["valid_images"])}</div>
            </div>
            """, unsafe_allow_html=True)

        with c2:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">INVALID IMAGES</div>
                <div class="metric-value">{len(d["invalid_images"])}</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("### Animal Class Distribution")

        st.bar_chart(d["class_counts"])

    else:
        st.info("Dataset inspection file is not available.")


# ---------------- MODEL INFORMATION ----------------

elif page == "Model Information":

    st.markdown(
        '<div class="section-title">About MobileNetV2</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="info-card">
        <h3>🧠 MobileNetV2 Architecture</h3>
        MobileNetV2 is a lightweight convolutional neural network
        designed for efficient image recognition.
        <br><br>
        <b>Features:</b>
        <ul>
            <li>ImageNet pretrained weights</li>
            <li>Transfer learning</li>
            <li>Feature extraction</li>
            <li>Global Average Pooling</li>
            <li>Dropout regularization</li>
            <li>Softmax classification output</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    metadata = MODEL_DIR / "mobilenetv2_metadata.json"

    if metadata.exists():

        d = json.loads(metadata.read_text())

        st.markdown("### Training Details")

        st.json(d)


# ---------------- PROJECT INFORMATION ----------------

else:

    st.markdown(
        '<div class="section-title">Project Information</div>',
        unsafe_allow_html=True
    )

    details = {
        "Project ID": PROJECT_ID,
        "Project Name": "Multi-Class Animal Image Classification",
        "University": "Invertis University, Bareilly",
        "Department": "CSE",
        "Semester": "V",
        "Section": "E",
        "Group ID": "BTech_DL_051",
        "Mentor": "Pradeep Singh",
        "Technology": "Python, TensorFlow, Streamlit",
        "Model": "MobileNetV2"
    }

    for key, value in details.items():

        st.markdown(f"""
        <div class="info-card">
            <span style="color:#75819a">{key}</span>
            <br>
            <b style="color:#173d7a">{value}</b>
        </div>
        """, unsafe_allow_html=True)


# ---------------- FOOTER ----------------

st.markdown("---")

st.markdown(
    "<center style='color:#8490a5;font-size:12px'>"
    "AnimalVision AI | DL-029 | Powered by Deep Learning"
    "</center>",
    unsafe_allow_html=True
)
