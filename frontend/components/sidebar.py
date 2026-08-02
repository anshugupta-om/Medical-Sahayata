import streamlit as st


def sidebar():

    st.sidebar.title("🏥 Medical Sahayata")

    page = st.sidebar.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "📤 Upload Report",
            "💬 AI Chat",
            "📄 Report History",
            "👤 Profile"
        ]
    )

    st.sidebar.divider()

    if st.sidebar.button("🚪 Logout"):

        del st.session_state.token
        st.rerun()

    return page