import streamlit as st
st.set_page_config(page_title="RogueShield: AI Threat Detection", layout="wide")

import pandas as pd
import numpy as np
from model_loader import load_models
from utils import read_and_validate_csv, prepare_input

# Page config
st.title("RogueShield: Real-Time AI Threat Detection")

# Intro section
st.markdown("""
**RogueShield** is an AI-powered intrusion detection system that leverages deep learning to identify, classify, and explain malicious network behavior in real-time.  
This tool uses two models:
- A preprocessing model to encode and format raw network data
- A classifier trained to detect multiple types of attacks based on the NSL-KDD dataset

Upload your network traffic CSV below to get instant predictions and insights on potential threats.
""")

# Class labels
class_names = [
    'Analysis','Backdoor','DoS','Exploits','Fuzzers',
    'Generic','Normal','Reconnaissance','Shellcode','Worms'
]

# Load models
preproc_model, intr_model = load_models()

# Determine required features
expected_features = [inp.name.split(":")[0] for inp in preproc_model.inputs]
categorical_features = ['proto', 'service', 'state']

# File upload
uploaded = st.file_uploader("Upload network traffic CSV", type="csv")
if uploaded:
    try:
        df = read_and_validate_csv(uploaded, expected_features)
        st.success("File loaded and validated.")
        st.subheader("Input Preview")
        st.dataframe(df.head())
        st.write("Column types:")
        st.write(df.dtypes)

        # Prepare input
        X_dict = prepare_input(df, expected_features, categorical_features)

        # Predict
        X_all = preproc_model.predict(X_dict)
        yhat = intr_model.predict(X_all)

        # Extract predictions
        idxs = np.argmax(yhat, axis=1)
        conf = yhat.max(axis=1)
        labels = [class_names[i] for i in idxs]

        # Display
        results = pd.DataFrame({
            "Predicted Class": labels[:10],
            "Confidence": np.round(conf[:10], 3)
        })
        st.subheader("Top-10 Predictions")
        st.dataframe(results)

        # Download
        csv = results.to_csv(index=False).encode()
        st.download_button("⬇️ Download CSV", data=csv, file_name="rogueshield_predictions.csv")

    except Exception as e:
        st.error(f"Error: {e}")
