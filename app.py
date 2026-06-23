import streamlit as st
import pandas as pd
import joblib

# Load model

model = joblib.load("diabetes_model.pkl")

# Page title

st.set_page_config(
page_title="Diabetes Prediction System",
page_icon="🩺"
)

st.title("🩺 Diabetes Prediction System")
st.write("Enter patient details below")

# Inputs

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

# Predict button

if st.button("Predict"):

    
    input_data = pd.DataFrame({
    "age": [age],
    "hypertension": [hypertension],
    "heart_disease": [heart_disease],
    "bmi": [bmi],
    "HbA1c_level": [hba1c],
    "blood_glucose_level": [blood_glucose],
    "gender_Male": [1 if gender == "Male" else 0],
    "gender_Other": [1 if gender == "Other" else 0],
    "smoking_history_current": [1 if smoking_history == "current" else 0],
    "smoking_history_ever": [1 if smoking_history == "ever" else 0],
    "smoking_history_former": [1 if smoking_history == "former" else 0],
    "smoking_history_never": [1 if smoking_history == "never" else 0],
    "smoking_history_not current": [1 if smoking_history == "not current" else 0]
})
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]

    st.write("Prediction:", prediction)
    st.write("Probability:", probability)

    if prediction == 1:
        st.error("⚠️ Diabetic")
    else:
        st.success("✅ Not Diabetic")

    st.dataframe(input_data)