import requests
import streamlit as st

from config import BACKEND_URL


def show_register():

    st.title(" Create Account")

    name = st.text_input(
        "Full Name",
        key="register_name"
    )

    email = st.text_input(
        "Email",
        key="register_email"
    )
    
    phone = st.text_input(
        "Phone Number",
        key="register_phone"
    )

    password = st.text_input(
        "Password",
        type="password",
        key="register_password"
    )

    confirm_password = st.text_input(
        "Confirm Password",
        type="password",
        key="register_confirm_password"
    )

    if st.button("Register", key="register_button"):

        if not name or not email or not phone or not password:
            st.error("Please fill all fields.")
            return

        if password != confirm_password:
            st.error("Passwords do not match.")
            return

        response = requests.post(
            f"{BACKEND_URL}/api/v1/auth/register",
            json={
                "name": name,
                "email": email,
                "phone": phone,
                "password": password
            }
        )

        if response.status_code == 200:

            st.success("Registration successful!")

            st.info("Please login with your account.")

            st.session_state.page = "login"

            st.rerun()

        else:

            try:
                detail = response.json().get("detail", response.text)
            except Exception:
                detail = response.text

            st.error(detail)