import streamlit as st
import pickle
import numpy as np
import datetime
from commons import *

# Load the Saved Model
loaded_model = pickle.load(open("trainedModel.sav", "rb"))


# Create a Function for Prediction
def hypertensionRiskPrediction(inputData):
    inputDataAsNumpyArray = np.asarray(inputData)
    inputDataReshaped = inputDataAsNumpyArray.reshape(1, -1)
    prediction = loaded_model.predict(inputDataReshaped)

    # return "Good Health"
    if prediction[0] == 0:
        return "Good Health"
    elif prediction[0] == 1:
        return "Mild Risk of Hypertension"
    elif prediction[0] == 2:
        return "High Risk of Hypertension"
    else:
        return "Error! Verify Input."


def prediction():
    st.markdown("<h1> Check Health Status</h1>", unsafe_allow_html=True)
    st.info("Input result.")

    gender = st.selectbox(
        "Gender",
        ["Select", "Male", "Female"],
    )
    gender = 1 if gender == "Male" else (0 if gender == "Female" else "Select")
    age = st.number_input(
        "Age",
        min_value=0,
        max_value=120,
        step=1,
    )
    systolic_bp = st.number_input(
        "Systolic BP",
        min_value=0,
        max_value=300,
        step=1,
    )
    diastolic_bp = st.number_input(
        "Diastolic BP",
        min_value=0,
        max_value=200,
        step=1,
    )
    height = st.number_input(
        "Height (cm)",
        min_value=0.0,
        max_value=250.0,
        step=0.1,
    )
    weight = st.number_input(
        "Weight (kg)",
        min_value=0.0,
        max_value=200.0,
        step=0.1,
    )

    # Calculate BMI
    bmi = weight / (height / 100) ** 2 if height > 0 else 0

    st.write(f"Calculated BMI: {bmi:.2f}")

    diagnosis = ""

    if st.button("CHECK STATUS"):
        if (
            gender == "Select"
            or age == 0
            or systolic_bp == 0
            or diastolic_bp == 0
            or height == 0.0
            or weight == 0.0
            or bmi == 0.0
        ):
            st.warning("Please fill in all details.")
        else:
            diagnosis = hypertensionRiskPrediction(
                [gender, age, systolic_bp, diastolic_bp, bmi]
            )
            # store_patient_data(unique_id, gender, age, systolic_bp, diastolic_bp, bmi, diagnosis)
            gender = "Male" if gender == 1 else "Female"

    if diagnosis:  # Display diagnosis only if it is not empty
        st.success(diagnosis)

        MedicalDatas.create(
            uid=Us.user.id,
            age=age,
            gender=gender,
            systolic_bp=systolic_bp,
            diastolic_bp=diastolic_bp,
            height=height,
            weight=weight,
            bmi=bmi,
            diagnosis=diagnosis,
            timestamp=datetime.datetime.now().isoformat(),
        )
