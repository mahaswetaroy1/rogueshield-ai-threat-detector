import pandas as pd
import numpy as np
import streamlit as st

@st.cache_resource
def load_model():
    import tensorflow as tf
    return tf.keras.models.load_model("models/intrusion_classifier/rogueshield_intrusion_model.h5")

model = load_model()

# Define preprocessing helpers
def read_and_validate_csv(uploaded_file, expected_columns):
    """
    Validates uploaded CSV for expected columns and returns sanitized DataFrame.
    """
    try:
        df = pd.read_csv(uploaded_file)
        missing = [c for c in expected_columns if c not in df.columns]
        if missing:
            raise ValueError(f"Missing expected columns: {missing}")
        return df[expected_columns]
    except Exception as e:
        raise ValueError(f"CSV validation failed: {e}")

def prepare_input(df, expected_features, categorical_features=None):
    """
    Converts input DataFrame into model-friendly format (dict of float32 ndarrays).
    """
    try:
        df = df[expected_features]
        df = df.apply(pd.to_numeric, errors="coerce")
        df.dropna(inplace=True)

        for col in df.columns:
            if df[col].dtype == 'object':
                raise ValueError(f"Column '{col}' has invalid dtype: object")

        df = df.astype("float32")
        return {col: df[col].values.reshape(-1, 1) for col in df.columns}

    except Exception as e:
        raise ValueError(f"Input preparation failed: {str(e)}")

