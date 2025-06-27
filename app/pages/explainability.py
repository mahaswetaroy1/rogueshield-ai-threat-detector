import streamlit as st
import pandas as pd
import shap
import numpy as np
import matplotlib.pyplot as plt

from model_loader import load_models
from utils import read_and_validate_csv, prepare_input

st.set_page_config(page_title="RogueShield Explainability", layout="wide")
st.title("RogueShield Model Explainability")

st.markdown("""
This module uses **SHAP values** to explain why RogueShield's intrusion detection model predicted a packet as malicious.  
We also map top influential features to the **MITRE ATT&CK** framework (experimental).
""")

# Load models
preproc_model, intr_model = load_models()

# Class names
class_names = ['Analysis', 'Backdoor', 'DoS', 'Exploits', 'Fuzzers',
               'Generic', 'Normal', 'Reconnaissance', 'Shellcode', 'Worms']

# File Upload
uploaded_file = st.file_uploader("Upload a network CSV file", type="csv")
if uploaded_file:
    try:
        expected_features = [input.name.split(":")[0] for input in preproc_model.inputs]
        df = read_and_validate_csv(uploaded_file, expected_features)
        st.success("CSV loaded and validated.")
        st.dataframe(df.head())

        # Preprocess input
        categorical_features = ['proto', 'service', 'state']
        X_dict = prepare_input(df, expected_features, categorical_features)
        X_all = preproc_model.predict(X_dict)

        # Predict
        preds = intr_model.predict(X_all)
        pred_classes = np.argmax(preds, axis=1)

        # SHAP Explainability
        st.subheader("SHAP Global Summary")
        with st.spinner("Computing SHAP values..."):
            explainer = shap.Explainer(intr_model, X_all[:100])
            shap_values = explainer(X_all[:100])
            fig = shap.plots.beeswarm(shap_values, show=False)
            st.pyplot(bbox_inches="tight")

        # MITRE ATT&CK Mapping (experimental)
        st.subheader("MITRE ATT&CK Mapping (Experimental)")
        top_features = np.argsort(np.abs(shap_values.values).mean(0))[::-1][:5]
        for i in top_features:
            feat = expected_features[i]
            st.markdown(f"**Feature**: `{feat}` → Possible tactic: _[TBD — Manual Mapping]_")

    except Exception as e:
        st.error(f"Explainability error: {str(e)}")
