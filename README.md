# 🏦 Smart Lender

## AI Powered Loan Approval Prediction System

Smart Lender is a Machine Learning based web application that predicts whether a loan application is likely to be **Approved** or **Rejected** based on applicant details.

The project is developed using **Python**, **Flask**, **Scikit-Learn**, and **XGBoost**. It provides a simple web interface where users can enter applicant information and instantly receive a loan approval prediction.

---

# 📌 Project Overview

Financial institutions receive thousands of loan applications every day. Manually evaluating each application is time-consuming and may lead to inconsistent decisions.

Smart Lender helps automate this process by using Machine Learning algorithms trained on historical loan data.

The application predicts loan approval based on:

- Number of Dependents
- Education
- Self Employment
- Annual Income
- Loan Amount
- Loan Term
- CIBIL Score
- Residential Assets
- Commercial Assets
- Luxury Assets
- Bank Assets

---

# 🎯 Objectives

- Predict loan approval accurately.
- Reduce manual verification time.
- Assist banks in decision making.
- Improve customer experience.
- Demonstrate Machine Learning deployment using Flask.

---

# 🚀 Features

- User-friendly web interface
- Loan approval prediction
- Machine Learning based decision making
- Real-time prediction
- Responsive design
- Fast prediction
- High accuracy
- Secure input handling

---

# 🛠 Technologies Used

## Programming Language

- Python

## Frontend

- HTML5
- CSS3

## Backend

- Flask

## Libraries

- Pandas
- NumPy
- Scikit-Learn
- XGBoost
- Joblib

---

# 🤖 Machine Learning Algorithms

The project compares multiple classification algorithms.

- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)
- XGBoost (Best Performing Model)

The XGBoost model is selected as the final model for deployment.

---

# 📂 Project Structure

```
Smart-Lender/
│
├── app.py
├── requirements.txt
├── README.md
│
├── dataset/
│   ├── loan_approval_dataset.csv
│   └── cleaned_loan_dataset.csv
│
├── models/
│   ├── best_model.pkl
│   ├── scaler.pkl
│   ├── education_encoder.pkl
│   ├── employment_encoder.pkl
│   └── loan_encoder.pkl
│
├── templates/
│   ├── index.html
│   ├── predict.html
│   ├── result.html
│   └── about.html
│
├── static/
│   ├── css/
│   ├── images/
│   └── js/
│
├── preprocessing/
│
├── outputs/
│   ├── graphs/
│   └── screenshots/
│
└── documentation/
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Smart-Lender.git
```

Move into the project folder

```bash
cd Smart-Lender
```

Create virtual environment

```bash
python -m venv .venv
```

Activate virtual environment

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Flask application

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

# 📋 Input Parameters

The application accepts the following inputs:

- Dependents
- Education
- Self Employed
- Annual Income
- Loan Amount
- Loan Term
- CIBIL Score
- Residential Assets
- Commercial Assets
- Luxury Assets
- Bank Assets

---

# 📊 Output

The model predicts one of the following:

- ✅ Loan Approved
- ❌ Loan Rejected

---

# 📈 Machine Learning Pipeline

1. Data Collection
2. Data Cleaning
3. Data Preprocessing
4. Label Encoding
5. Feature Scaling
6. Train-Test Split
7. Model Training
8. Model Evaluation
9. Best Model Selection
10. Model Serialization
11. Flask Deployment

---

# 📸 Application Screenshots

Add screenshots inside:

```
outputs/screenshots/
```

Example:

- Home Page
- Prediction Page
- Approved Result
- Rejected Result
- About Page

---

# ☁ Future Enhancements

- User Authentication
- Database Integration
- Cloud Deployment
- Explainable AI
- PDF Report Generation
- Email Notifications
- Loan Eligibility Score
- REST API Support

---

# 👨‍💻 Developed By

**Vartha Varalakshmi**

Team Lead – Smart Lender

Artificial Intelligence & Machine Learning

---

# 📄 License

This project is developed for educational and academic purposes.