import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load cleaned dataset
df = pd.read_csv("dataset/cleaned_loan_dataset.csv")

encoder = LabelEncoder()

categorical_columns = [
    "education",
    "self_employed",
    "loan_status"
]

for column in categorical_columns:
    df[column] = encoder.fit_transform(df[column])

print(df.head())

# Save encoded dataset
df.to_csv("dataset/encoded_dataset.csv", index=False)

print("Encoding Completed Successfully")