import tensorflow as tf
import streamlit as st

@st.cache_resource
def load_models():
    """
    Loads the preprocessing and intrusion detection models.
    Uses Streamlit's cache to avoid reloading on every interaction.
    """
    try:
        preprocessing_model = tf.keras.models.load_model("models/preprocessing_model.keras")
        intrusion_model = tf.keras.models.load_model("models/intrusion_classifier/rogueshield_intrusion_model.h5")
        return preprocessing_model, intrusion_model
    except Exception as e:
        st.error(f"Failed to load models: {e}")
        raise

