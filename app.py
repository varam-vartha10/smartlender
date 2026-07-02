from flask import Flask, render_template, request

from utils.model_loader import (
    load_model,
    load_scaler,
    load_education_encoder,
    load_employment_encoder,
    load_loan_encoder,
)

from utils.helper import prepare_input
from utils.validation import validate_inputs

# ==========================================
# Load Trained Model and Encoders
# ==========================================

model = load_model()
scaler = load_scaler()

education_encoder = load_education_encoder()
employment_encoder = load_employment_encoder()
loan_encoder = load_loan_encoder()

# ==========================================
# Create Flask App
# ==========================================

app = Flask(__name__)

# ==========================================
# Home Page
# ==========================================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================================
# About Page
# ==========================================

@app.route("/about")
def about():
    return render_template("about.html")


# ==========================================
# Prediction Page
# ==========================================

@app.route("/predict")
def predict_page():
    return render_template("predict.html")


# ==========================================
# Prediction Result
# ==========================================

@app.route("/result", methods=["POST"])
def result():

    try:

        # ==============================
        # Get Form Data
        # ==============================

        dependents = int(request.form["dependents"])

        education = education_encoder.transform(
            [request.form["education"]]
        )[0]

        self_employed = employment_encoder.transform(
            [request.form["self_employed"]]
        )[0]

        income_annum = int(request.form["income_annum"])
        loan_amount = int(request.form["loan_amount"])
        loan_term = int(request.form["loan_term"])
        cibil_score = int(request.form["cibil_score"])

        residential_assets = int(request.form["residential_assets_value"])
        commercial_assets = int(request.form["commercial_assets_value"])
        luxury_assets = int(request.form["luxury_assets_value"])
        bank_assets = int(request.form["bank_asset_value"])

        # ==============================
        # Validate Inputs
        # ==============================

        input_data = {
            "income_annum": income_annum,
            "loan_amount": loan_amount,
            "loan_term": loan_term,
            "cibil_score": cibil_score,
        }

        valid, message = validate_inputs(input_data)

        if not valid:
            return render_template("error.html", error=message)

        # ==============================
        # Prepare Input
        # ==============================

        data = prepare_input(
            dependents,
            education,
            self_employed,
            income_annum,
            loan_amount,
            loan_term,
            cibil_score,
            residential_assets,
            commercial_assets,
            luxury_assets,
            bank_assets,
        )

        # ==============================
        # Scale Features
        # ==============================

        data = scaler.transform(data)

        # ==============================
        # Predict
        # ==============================

        prediction = model.predict(data)

        prediction = loan_encoder.inverse_transform(prediction)[0]

        # ==============================
        # Show Result
        # ==============================

        return render_template(
            "result.html",
            prediction=prediction,
        )

    except Exception as e:

        return render_template(
            "error.html",
            error=str(e),
        )


# ==========================================
# Run Flask App
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)