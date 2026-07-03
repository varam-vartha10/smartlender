import joblib
import os


def load_scaler():
    scaler_path = os.path.join("model", "scaler.pkl")

    if os.path.exists(scaler_path):
        return joblib.load(scaler_path)

    return None


def scale_data(df):
    scaler = load_scaler()

    if scaler:
        return scaler.transform(df)

    return df