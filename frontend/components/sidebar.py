import streamlit as st


def sidebar():

    st.sidebar.title("Medical Sahayata")
    languages = [
        "English",
        "Hindi",
        "Bengali",
        "Telugu",
        "Marathi",
        "Tamil",
        "Gujarati",
        "Kannada",
        "Malayalam",
        "Punjabi",
        "Odia",
        "Assamese",
        "Urdu",
        "Nepali",
        "Sanskrit",
    ]

    selected_language = st.sidebar.selectbox(
        "Language",
        languages,
        key="language"
    )

    page = st.sidebar.radio(
        "Navigation",
        [
            "Dashboard",
            "Upload Report",
            "AI Chat",
            "Report History",
            "Profile"
        ]
    )

    st.sidebar.divider()

    if st.sidebar.button("Logout"):

        del st.session_state.token
        st.rerun()

    return page