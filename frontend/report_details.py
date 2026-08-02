import requests
import streamlit as st

from config import BACKEND_URL


def show_report_details():

    report_id = st.session_state.get("selected_report")

    if report_id is None:
        st.info("Select a report from Report History.")
        return

    headers = {
        "Authorization": f"Bearer {st.session_state.token}"
    }

    response = requests.get(
        f"{BACKEND_URL}/api/v1/report/{report_id}",
        headers=headers
    )

    if response.status_code != 200:
        st.error("Unable to load report.")
        return

    report = response.json()
    data = report["structured_data"]

    st.title("📄 Medical Report Details")

    st.subheader(report["filename"])

    st.write(f"**Uploaded:** {report['uploaded_at']}")

    st.divider()

    st.subheader("👤 Patient")

    st.write(f"**Name:** {data.get('patient_name', 'N/A')}")
    st.write(f"**Age:** {data.get('age', 'N/A')}")
    st.write(f"**Gender:** {data.get('gender', 'N/A')}")

    st.divider()

    st.subheader("🏥 Hospital")

    st.write(data.get("hospital", "N/A"))

    st.write(f"**Doctor:** {data.get('doctor', 'N/A')}")

    st.divider()

    st.subheader("🩺 Diagnosis")

    st.success(data.get("diagnosis", "N/A"))

    st.divider()

    st.subheader("💊 Medicines")

    for medicine in data.get("medicines", []):
        st.write(f"✔ {medicine}")

    st.divider()

    st.subheader("🧪 Laboratory Results")

    lab_results = data.get("laboratory_results", {})

    if lab_results:
        st.table(
            {
                "Test": list(lab_results.keys()),
                "Result": list(lab_results.values())
            }
        )

    st.divider()

    st.subheader("📄 AI Summary")

    st.write(report["summary"])

    if st.button("⬅ Back to Report History"):
        del st.session_state.selected_report
        st.rerun()