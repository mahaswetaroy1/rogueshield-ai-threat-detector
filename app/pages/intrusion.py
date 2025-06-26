import streamlit as st
import pandas as pd
import numpy as np
from model_loader import load_models
from utils import read_and_validate_csv, prepare_input


st.set_page_config(page_title="Intrusion Detection", layout="wide")
st.title("RogueShield: Real-Time Intrusion Detection")

# Load models
preprocessing_model, intrusion_model = load_models()
expected_features = [input.name.split(":")[0] for input in preprocessing_model.inputs]


# Upload CSV file
uploaded_file = st.file_uploader("Upload network traffic CSV", type=["csv"])

if uploaded_file:
    try:
        # Read and validate CSV
        df = read_and_validate_csv(uploaded_file, expected_features)
        st.success("File loaded successfully")
        st.write("### Input Preview:")
        st.dataframe(df.head())

        # Prepare model input
        X_dict = prepare_input(df)
        X_all = preprocessing_model.predict(X_dict)

        # Predict using intrusion model
        y_pred = intrusion_model.predict(X_all)
        y_class = np.argmax(y_pred, axis=1)
        y_conf = y_pred.max(axis=1)

        # Display Results
        class_names = ['Analysis', 'Backdoor', 'DoS', 'Exploits', 'Fuzzers',
                       'Generic', 'Normal', 'Reconnaissance', 'Shellcode', 'Worms']
        predicted_labels = [class_names[i] for i in y_class]

        results_df = pd.DataFrame({
            "Predicted Class": predicted_labels,
            "Confidence": y_conf.round(3)
        })

        st.write("### Prediction Results (Top 10 Rows):")
        st.dataframe(results_df.head(10))

    except Exception as e:
        st.error(f"Error: {e}")

