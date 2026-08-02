import requests
import streamlit as st

from config import BACKEND_URL


def show_history_page():

    st.title("📄 Report History")

    headers = {
        "Authorization": f"Bearer {st.session_state.token}"
    }

    response = requests.get(
        f"{BACKEND_URL}/api/v1/history/reports",
        headers=headers
    )

    if response.status_code != 200:
        st.error("Unable to load report history.")
        return

    reports = response.json()

    if not reports:
        st.info("No reports uploaded yet.")
        return

    for report in reports:

        with st.container(border=True):

            st.subheader(report["filename"])

            st.write(f"**Uploaded:** {report['uploaded_at']}")

            if st.button(
                "View Details",
                key=report["id"]
            ):
                st.session_state.selected_report = report["id"]
                st.rerun()