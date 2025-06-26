import streamlit as st
import pandas as pd
import numpy as np
from model_loader import load_models
from utils import read_and_validate_csv, prepare_input

st.set_page_config(page_title="RogueShield: AI Threat Detection", layout="wide")
st.title("RogueShield: Real-Time Intrusion Detection")

class_names = [
    'Analysis','Backdoor','DoS','Exploits','Fuzzers',
    'Generic','Normal','Reconnaissance','Shellcode','Worms'
]

# 1) load your two models (preprocessing first, then classifier)
preproc_model, intr_model = load_models()

# 2) extract the raw input names (strip the “:0”)
expected_features = [inp.name.split(":")[0] for inp in preproc_model.inputs]

# 3) tell it which of those are truly categorical
categorical_features = ['proto','service','state']

uploaded = st.file_uploader("Upload network traffic CSV", type="csv")
if uploaded:
    try:
        df = read_and_validate_csv(uploaded, expected_features)
        st.success("File loaded and validated.")
        st.subheader("Input Preview");  st.dataframe(df.head())

        # prepare input → dict[str→ndarray]
        X_dict = prepare_input(df, expected_features, categorical_features)

        # run through your Keras pipelines
        X_all  = preproc_model.predict(X_dict)
        yhat   = intr_model.predict(X_all)

        # pick off the top‐classes
        idxs   = np.argmax(yhat, axis=1)
        conf   = yhat.max(axis=1)
        labels = [class_names[i] for i in idxs]

        # show the first 10
        res = pd.DataFrame({
           "Predicted Class": labels[:10],
           "Confidence":     np.round(conf[:10],3)
        })
        st.subheader("Top-10 Predictions");  st.dataframe(res)

        csv = res.to_csv(index=False).encode()
        st.download_button("Download CSV", data=csv, file_name="predictions.csv")

    except Exception as e:
        st.error(f"Error: {e}")
