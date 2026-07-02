# ==========================================
# SMART LENDER - MODEL TRAINING
# ==========================================
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

print("=" * 50)
print("SMART LENDER - LOAN APPROVAL PREDICTION")
print("=" * 50)

# ------------------------------------------
# Load Dataset
# ------------------------------------------

df = pd.read_csv("dataset/loan_approval_dataset.csv")

# Remove spaces from column names
df.columns = df.columns.str.strip()

# Remove spaces from text values
for column in df.select_dtypes(include="object").columns:
    df[column] = df[column].str.strip()

print("\nDataset Loaded Successfully")
print(df.head())

print("\nDataset Shape :", df.shape)

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows :", df.duplicated().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

print("\nDuplicates Removed Successfully")

# ------------------------------------------
# Encode Categorical Columns
# ------------------------------------------

print("\nEncoding categorical columns...")

education_encoder = LabelEncoder()
employment_encoder = LabelEncoder()
loan_encoder = LabelEncoder()

df["education"] = education_encoder.fit_transform(df["education"])
df["self_employed"] = employment_encoder.fit_transform(df["self_employed"])
df["loan_status"] = loan_encoder.fit_transform(df["loan_status"])

print("Encoding Completed Successfully")
# Save encoders
joblib.dump(education_encoder, "models/education_encoder.pkl")
joblib.dump(employment_encoder, "models/employment_encoder.pkl")
joblib.dump(loan_encoder, "models/loan_encoder.pkl")

print("Encoders Saved Successfully")

# ------------------------------------------
# Feature Selection
# ------------------------------------------

X = df.drop(["loan_id", "loan_status"], axis=1)
y = df["loan_status"]

print("\nFeatures Shape :", X.shape)
print("Target Shape :", y.shape)

# ------------------------------------------
# Train Test Split
# ------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining Samples :", X_train.shape[0])
print("Testing Samples :", X_test.shape[0])

# ------------------------------------------
# Feature Scaling
# ------------------------------------------

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print("\nFeature Scaling Completed")

# Save scaler
joblib.dump(scaler, "models/scaler.pkl")

print("Scaler Saved Successfully")
# ------------------------------------------
# Model Training
# ------------------------------------------

print("\n" + "=" * 50)
print("TRAINING MACHINE LEARNING MODELS")
print("=" * 50)

models = {
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(random_state=42),
    "KNN": KNeighborsClassifier(),
    "XGBoost": XGBClassifier(
        random_state=42,
        eval_metric="logloss"
    )
}

results = {}

best_model = None
best_accuracy = 0
best_model_name = ""

for name, model in models.items():

    print(f"\nTraining {name}...")

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    results[name] = accuracy

    print(f"{name} Accuracy : {accuracy:.4f}")

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = model
        best_model_name = name

print("\n" + "=" * 50)
print("MODEL COMPARISON")
print("=" * 50)

for model_name, accuracy in results.items():
    print(f"{model_name:20} : {accuracy:.4f}")

print("\nBest Model :", best_model_name)
print("Best Accuracy :", round(best_accuracy * 100, 2), "%")

# Save Best Model
joblib.dump(best_model, "models/best_model.pkl")

print("\nBest Model Saved Successfully")

# Classification Report
predictions = best_model.predict(X_test)

print("\nClassification Report")
print(classification_report(y_test, predictions))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, predictions))