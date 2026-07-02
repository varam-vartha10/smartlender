import joblib

def test_model_loading():
    model = joblib.load("models/best_model.pkl")
    assert model is not None