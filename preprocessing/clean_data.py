import pandas as pd

# Load dataset
df = pd.read_csv("dataset/loan_approval_dataset.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Remove leading/trailing spaces from string values
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

print("Dataset Loaded Successfully\n")

print("Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df.drop_duplicates(inplace=True)

print("\nDuplicates Removed")

# Save cleaned dataset
df.to_csv("dataset/cleaned_loan_dataset.csv", index=False)

print("\nCleaned dataset saved successfully.")