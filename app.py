import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("diabetes_model.pkl")

st.title("🩺 Diabetes Prediction System")

st.write("Enter patient details below:")

# User Inputs
gender = st.selectbox(
    "Gender",
    ["Female", "Male", "Other"]
)

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

    # Create dataframe with EXACT columns used during training
    input_data = pd.DataFrame(
        0,
        index=[0],
        columns=[
            'age',
            'hypertension',
            'heart_disease',
            'bmi',
            'HbA1c_level',
            'blood_glucose_level',
            'gender_Male',
            'gender_Other',
            'smoking_history_current',
            'smoking_history_ever',
            'smoking_history_former',
            'smoking_history_never',
            'smoking_history_not current'
        ]
    )

    # Numeric values
    input_data['age'] = age
    input_data['hypertension'] = hypertension
    input_data['heart_disease'] = heart_disease
    input_data['bmi'] = bmi
    input_data['HbA1c_level'] = hba1c
    input_data['blood_glucose_level'] = blood_glucose

    # Gender encoding
    if gender == "Male":
        input_data['gender_Male'] = 1
    elif gender == "Other":
        input_data['gender_Other'] = 1

    # Smoking history encoding
    if smoking_history == "current":
        input_data['smoking_history_current'] = 1
    elif smoking_history == "ever":
        input_data['smoking_history_ever'] = 1
    elif smoking_history == "former":
        input_data['smoking_history_former'] = 1
    elif smoking_history == "never":
        input_data['smoking_history_never'] = 1
    elif smoking_history == "not current":
        input_data['smoking_history_not current'] = 1

    try:
        prediction = model.predict(input_data)

        if prediction[0] == 1:
            st.error("⚠️ Diabetic")
        else:
            st.success("✅ Not Diabetic")

    except Exception as e:
        st.error(f"Prediction Error: {e}")