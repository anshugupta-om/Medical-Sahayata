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
from register import show_register
from login import show_login
load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL")

st.set_page_config(
    page_title="Medical Sahayata",
    page_icon="",
    layout="wide"
)

st.title("Medical Sahayata")

# ------------------------
# Login Section
# ------------------------
if "page" not in st.session_state:
    st.session_state.page = "login"

if "token" not in st.session_state:

    login_tab, register_tab = st.tabs(
        [" Login", " Register"]
    )

    with login_tab:
        show_login()

    with register_tab:
        show_register()



else:

    # Show Dashboard
    page = sidebar()

    if page == "Dashboard":
        show_dashboard()

    elif page == "Upload Report":
        show_upload_page()

    elif page == "AI Chat":
        show_chat_page()

    elif page == "Report History":

        if "selected_report" in st.session_state:
            show_report_details()
        else:
            show_history_page()

    elif page == "Profile":
        st.header("Profile")
        st.info("Coming in next step...")

    