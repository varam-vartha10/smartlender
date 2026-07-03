import pandas as pd


def create_features(df: pd.DataFrame):
    """
    Create new engineered features.
    """

    # Total Income
    df["TotalIncome"] = (
        df["ApplicantIncome"] +
        df["CoapplicantIncome"]
    )

    # EMI Estimate
    df["EMI"] = (
        df["LoanAmount"] /
        df["Loan_Amount_Term"]
    )

    # Income per Loan
    df["IncomePerLoan"] = (
        df["TotalIncome"] /
        (df["LoanAmount"] + 1)
    )

    return df