import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf

st.set_page_config(page_title="RogueShield Category Forecasting", layout="wide")
st.title("RogueShield: Attack Category Forecasting")

st.markdown("""
This module forecasts **future trends in attack categories** using a trained LSTM model.  
It helps analysts anticipate which types of threats are likely to rise in frequency based on past behavior.
""")

# Load LSTM model
try:
    model = tf.keras.models.load_model("models/category_forecast/lstm_category_forecast.h5")
except Exception as e:
    st.error(f"Failed to load forecasting model: {e}")
    st.stop()

# Upload Data
uploaded_file = st.file_uploader("Upload a time-series CSV (e.g. counts per attack type)", type="csv")
if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("File uploaded successfully.")
        st.dataframe(df.head())

        # Assume last N rows as input for forecasting
        sequence = df.values[-30:].astype("float32").reshape(1, 30, -1)

        # Forecast next step
        prediction = model.predict(sequence)
        pred_df = pd.DataFrame(prediction[0], columns=df.columns)
        st.subheader("Forecasted Category Distribution")
        st.dataframe(pred_df.T.rename(columns={0: "Predicted Proportion"}))

        st.bar_chart(pred_df.T)

    except Exception as e:
        st.error(f"Forecasting error: {e}")
