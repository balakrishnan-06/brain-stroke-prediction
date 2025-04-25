
import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🧠 Brain Stroke Prediction App")

st.markdown("Please enter the following details:")

# Collect user input
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
age = st.slider("Age", 0, 100, 30)
hypertension = st.selectbox("Hypertension", [0, 1])
heart_disease = st.selectbox("Heart Disease", [0, 1])
ever_married = st.selectbox("Ever Married", ["Yes", "No"])
work_type = st.selectbox("Work Type", ["Private", "Self-employed", "Govt_job", "children", "Never_worked"])
residence_type = st.selectbox("Residence Type", ["Urban", "Rural"])
avg_glucose_level = st.slider("Average Glucose Level", 50.0, 300.0, 100.0)
bmi = st.slider("BMI", 10.0, 50.0, 25.0)
smoking_status = st.selectbox("Smoking Status", ["formerly smoked", "never smoked", "smokes", "Unknown"])

# Convert inputs to DataFrame
input_data = pd.DataFrame({
    'gender': [gender],
    'age': [age],
    'hypertension': [hypertension],
    'heart_disease': [heart_disease],
    'ever_married': [ever_married],
    'work_type': [work_type],
    'Residence_type': [residence_type],
    'avg_glucose_level': [avg_glucose_level],
    'bmi': [bmi],
    'smoking_status': [smoking_status]
})

# Make prediction
if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("⚠️ High risk of stroke!")
    else:
        st.success("✅ Low risk of stroke.")
