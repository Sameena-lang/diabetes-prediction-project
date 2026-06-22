import streamlit as st

st.title("Diabetes Prediction System")

st.write("This is my Machine Learning project.")

age = st.number_input("Enter Age")

if st.button("Predict"):
    st.success("Prediction completed")