import os
import requests
import streamlit as st
from dotenv import load_dotenv
from dashboard import show_dashboard
from components.sidebar import sidebar
from upload import show_upload_page
from chat import show_chat_page
from history import show_history_page
from report_details import show_report_details
load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL")

st.set_page_config(
    page_title="Medical Sahayata",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Medical Sahayata")

# ------------------------
# Login Section
# ------------------------

if "token" not in st.session_state:

    st.subheader("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        response = requests.post(
            f"{BACKEND_URL}/api/v1/auth/login",
            json={
                "email": email,
                "password": password
            }
        )

        if response.status_code == 200:

            st.session_state.token = response.json()["access_token"]
            st.rerun()

        else:
            st.error("Invalid credentials")

# ------------------------
# Chat Section
# ------------------------

else:

    # Show Dashboard
    page = sidebar()

    if page == "🏠 Dashboard":
        show_dashboard()

    elif page == "📤 Upload Report":
        show_upload_page()

    elif page == "💬 AI Chat":
        show_chat_page()

    elif page == "📄 Report History":

        if "selected_report" in st.session_state:
            show_report_details()
        else:
            show_history_page()

    elif page == "👤 Profile":
        st.header("Profile")
        st.info("Coming in next step...")

    st.divider()

    # Existing Chat
    st.subheader("💬 Medical Consultation")

    question = st.text_area("Ask your medical question:")

    if st.button("Consult"):

        headers = {
            "Authorization": f"Bearer {st.session_state.token}"
        }

        response = requests.post(
            f"{BACKEND_URL}/api/v1/medical/consult",
            json={
                "query": question
            },
            headers=headers
        )

        if response.status_code == 200:

            st.subheader("Response")

            st.write(
                response.json()["response"]
            )

        else:

            st.error(response.text)

    if st.button("Logout"):

        del st.session_state.token
        st.rerun()