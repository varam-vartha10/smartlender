from sklearn.preprocessing import LabelEncoder

def encode_columns(df):
    education = LabelEncoder()
    employment = LabelEncoder()
    loan = LabelEncoder()

    df["education"] = education.fit_transform(df["education"])
    df["self_employed"] = employment.fit_transform(df["self_employed"])
    df["loan_status"] = loan.fit_transform(df["loan_status"])

    return df