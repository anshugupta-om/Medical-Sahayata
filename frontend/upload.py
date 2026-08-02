import requests
import streamlit as st

from config import BACKEND_URL


def show_upload_page():

    st.title("📤 Upload Medical Report")

    uploaded_file = st.file_uploader(
        "Choose a PDF report",
        type=["pdf"]
    )

    if uploaded_file is None:
        return

    st.success(f"Selected: {uploaded_file.name}")

    if st.button("Upload Report"):

        headers = {
            "Authorization": f"Bearer {st.session_state.token}"
        }

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file,
                "application/pdf"
            )
        }

        with st.spinner("Uploading and processing report..."):

            response = requests.post(
                f"{BACKEND_URL}/api/v1/report/upload",
                headers=headers,
                files=files
            )

        if response.status_code == 200:

            st.success("✅ Report uploaded successfully!")

            data = response.json()

            st.write("### Processing Result")

            st.write(f"Pages : {data['pages']}")
            st.write(f"Chunks : {data['chunks']}")

            # Refresh dashboard data next time it is opened
            st.info("You can now open the Dashboard to view the AI analysis.")

        else:

            st.error(response.text)