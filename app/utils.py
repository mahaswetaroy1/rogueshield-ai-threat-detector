import pandas as pd
import numpy as np

def read_and_validate_csv(uploaded_file, expected_columns):
    """
    Reads the CSV, ensures all expected_columns are present,
    and returns a DataFrame with exactly those columns (in order).
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
    Prepares input for TensorFlow model:
    - Categorical features as string
    - All others coerced to float32
    """

    cats = set(categorical_features or [])
    nums = [c for c in expected_features if c not in cats]

    df = df[expected_features].copy()

    # Strip whitespace from everything
    df = df.applymap(lambda x: str(x).strip() if isinstance(x, str) else x)

    # Coerce numerics
    for c in nums:
        df[c] = pd.to_numeric(df[c], errors="coerce").astype(np.float32)

    for c in cats:
        df[c] = df[c].astype(str)

    # Catch any conversion failures
    if df[nums].dtypes.eq("object").any():
        raise ValueError("Non-numeric values found in numeric columns.")

    if df[nums].isnull().any().any():
        raise ValueError("NaNs found in numeric columns after coercion.")

    return {c: df[c].values.reshape(-1, 1) for c in expected_features}

