import pandas as pd


def encode_features(df: pd.DataFrame):
    """
    Encode categorical columns to numerical values.
    """

    mappings = {
        "Gender": {
            "Male": 1,
            "Female": 0
        },

        "Married": {
            "Yes": 1,
            "No": 0
        },

        "Education": {
            "Graduate": 1,
            "Not Graduate": 0
        },

        "Self_Employed": {
            "Yes": 1,
            "No": 0
        },

        "Property_Area": {
            "Urban": 2,
            "Semiurban": 1,
            "Rural": 0
        }
    }

    for column, mapping in mappings.items():
        if column in df.columns:
            df[column] = df[column].map(mapping)

    return df