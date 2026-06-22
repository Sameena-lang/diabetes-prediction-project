import streamlit as st

st.title("Diabetes Prediction System")

st.write("Enter patient details below:")

# Input Features
gender = st.selectbox("Gender", ["Male", "Female"])

age = st.number_input("Age", min_value=0, max_value=120, value=25)

hypertension = st.selectbox("Hypertension", [0, 1])

heart_disease = st.selectbox("Heart Disease", [0, 1])

smoking_history = st.selectbox(
    "Smoking History",
    ["never", "former", "current", "No Info"]
)

bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)

hba1c = st.number_input("HbA1c Level", min_value=3.0, max_value=15.0, value=5.5)

blood_glucose = st.number_input(
    "Blood Glucose Level",
    min_value=50,
    max_value=300,
    value=100
)

if st.button("Predict"):

    st.success("Patient details submitted successfully!")

    st.write("### Entered Details")

    st.write("Gender:", gender)
    st.write("Age:", age)
    st.write("Hypertension:", hypertension)
    st.write("Heart Disease:", heart_disease)
    st.write("Smoking History:", smoking_history)
    st.write("BMI:", bmi)
    st.write("HbA1c Level:", hba1c)
    st.write("Blood Glucose Level:", blood_glucose)

    st.info("Next step: Connect Random Forest model for prediction.")