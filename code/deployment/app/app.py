import os
import streamlit as st
import requests

ENDPOINT_URL = os.getenv("ENDPOINT_URL", "http://api:8000/inference")

st.title("Heart Disease prediction app")

age = st.text_input("Enter the age of the patient:")
sex = st.text_input("Enter the sex of the patient (male or female):")
cp = st.text_input("Enter the chest pain type (1-4):")
trestbps = st.text_input("Enter the resing blood pressure "
                         "(in mm Hg on admission to the hospital):")
chol = st.text_input("Enter the serum cholesterol (in mg/dl):")
fbs = st.text_input("Enter true if fasting blood sugar > 120 mg/dl,"
                    " else false:")
restecg = st.text_input("Enter resting electrocardiographic results (0-2):")
thalach = st.text_input("Enter maximum heart rate achieved")
exang = st.text_input("Enter true if there is exercise-induced angina,"
                      " else false:")
oldpeak = st.number_input("Enter ST depression induced by exercise relative"
                          " to rest:")
slope = st.text_input("Enter slope:")
ca = st.text_input("Enter ca:")
thal = st.text_input("Enter thal:")

if st.button("Send Request"):
    data = {
        "age": int(age),
        "sex": sex,
        "cp": int(cp),
        "trestbps": int(trestbps),
        "chol": int(chol),
        "fbs": True if fbs == "true" else False,
        "restecg": int(restecg),
        "thalach": int(thalach),
        "exang": True if fbs == "true" else False,
        "oldpeak": float(oldpeak),
        "slope": int(slope),
        "ca": int(ca),
        "thal": int(thal)
    }

    try:
        response = requests.post(ENDPOINT_URL, json=data)
    except requests.RequestException as e:
        st.error(f"An error occurred: {e}")

    if response.status_code == 200:
        data = response.json()
        prediction = data["prediction"]

        if prediction:
            st.subheader("There is a heart disease")
        else:
            st.subheader("There is no a heart disease")
    elif response.status_code == 422:
        st.error("Something wrong with data, please revise")
    else:
        st.error(f"Error: status code {response.status_code}")
