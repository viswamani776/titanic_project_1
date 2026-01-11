import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("linear_model.pkl")

st.title("💰 Salary Prediction App")
st.write("Predict salary based on years of experience")

# User input
experience = st.number_input(
    "Enter Years of Experience",
    min_value=0.0,
    max_value=50.0,
    step=0.5
)

# Prediction
if st.button("Predict Salary"):
    input_data = np.array([[experience]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Salary: ₹ {prediction[0]:,.2f}")
