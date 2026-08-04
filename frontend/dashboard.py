import os
import requests
import streamlit as st
from dotenv import load_dotenv
from config import BACKEND_URL
load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL")


def show_dashboard():

    st.title("Medical Sahayata Dashboard")

    headers = {
        "Authorization": f"Bearer {st.session_state.token}"
    }

    response = requests.get(
        f"{BACKEND_URL}/api/v1/dashboard/latest-report",
        headers=headers
    )

    if response.status_code != 200:
        st.warning("No medical report uploaded yet.")
        return

    report = response.json()

    data = report["structured_data"]

    st.subheader("Latest Report")

    st.write(report["original_filename"])

    st.divider()

    st.subheader("Patient Information")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Name**")
        st.write(data.get("patient_name", "N/A"))

        st.write("**Age**")
        st.write(data.get("age", "N/A"))

    with col2:

        st.write("**Gender**")
        st.write(data.get("gender", "N/A"))

        st.write("**Doctor**")
        st.write(data.get("doctor", "N/A"))

    st.divider()

    st.subheader("Hospital")

    st.write(data.get("hospital", "N/A"))

    st.divider()

    st.subheader("Diagnosis")

    st.success(data.get("diagnosis", "N/A"))

    st.divider()

    st.subheader("Medicines")

    medicines = data.get("medicines", [])

    if medicines:
        for medicine in medicines:
            st.write(f"✔ {medicine}")
    else:
        st.write("No medicines found.")

    st.divider()

    st.subheader("⚠ Risk Level")

    risk = data.get("risk_level", "Unknown")

    if risk.lower() == "low":
        st.success(risk)

    elif risk.lower() == "medium":
        st.warning(risk)

    elif risk.lower() == "high":
        st.error(risk)

    else:
        st.info(risk)

    st.divider()

    st.subheader("AI Summary")

    st.write(report["summary"])