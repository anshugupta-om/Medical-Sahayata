import requests
import streamlit as st

from config import BACKEND_URL


def show_login():

    st.subheader(" Login")

    email = st.text_input(
        "Email",
        key="login_email"
    )

    password = st.text_input(
        "Password",
        type="password",
        key="login_password"
    )

    if st.button("Login", key="login_button"):

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