import joblib


def load_model():
    return joblib.load("models/best_model.pkl")


def load_scaler():
    return joblib.load("models/scaler.pkl")


def load_education_encoder():
    return joblib.load("models/education_encoder.pkl")


def load_employment_encoder():
    return joblib.load("models/employment_encoder.pkl")


def load_loan_encoder():
    return joblib.load("models/loan_encoder.pkl")