def validate_inputs(data):
    """
    Basic validation for loan application inputs.
    """

    if data["income_annum"] <= 0:
        return False, "Income must be greater than zero."

    if data["loan_amount"] <= 0:
        return False, "Loan amount must be greater than zero."

    if data["loan_term"] <= 0:
        return False, "Loan term must be greater than zero."

    if data["cibil_score"] < 300 or data["cibil_score"] > 900:
        return False, "CIBIL Score must be between 300 and 900."

    return True, "Valid Input"