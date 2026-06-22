import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("diabetes_model.pkl")

st.title("🩺 Diabetes Prediction System")

st.write("Enter patient details below:")

# Inputs
gender = st.selectbox("Gender", ["Male", "Female"])

age = st.number_input(
    "Age",
    min_value=1,
    max_value=120,
    value=30
)

hypertension = st.selectbox(
    "Hypertension",
    [0, 1]
)

heart_disease = st.selectbox(
    "Heart Disease",
    [0, 1]
)

smoking_history = st.selectbox(
    "Smoking History",
    [
        "No Info",
        "never",
        "former",
        "current",
        "not current",
        "ever"
    ]
)

bmi = st.number_input(
    "BMI",
    min_value=10.0,
    max_value=60.0,
    value=25.0
)

hba1c = st.number_input(
    "HbA1c Level",
    min_value=3.0,
    max_value=15.0,
    value=5.5
)

blood_glucose = st.number_input(
    "Blood Glucose Level",
    min_value=50,
    max_value=300,
    value=100
)

if st.button("Predict"):

    input_data = pd.DataFrame({
        "gender": [gender],
        "age": [age],
        "hypertension": [hypertension],
        "heart_disease": [heart_disease],
        "smoking_history": [smoking_history],
        "bmi": [bmi],
        "HbA1c_level": [hba1c],
        "blood_glucose_level": [blood_glucose]
    })

    input_data = pd.get_dummies(input_data)

    try:
        prediction = model.predict(input_data)

        if prediction[0] == 1:
            st.error("⚠️ Diabetic")
        else:
            st.success("✅ Not Diabetic")

    except Exception as e:
        st.error(f"Prediction Error: {e}")