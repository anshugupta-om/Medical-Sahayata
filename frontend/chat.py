import requests
import streamlit as st

from config import BACKEND_URL


def show_chat_page():

    st.title("💬 AI Medical Chat")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous messages
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    prompt = st.chat_input(
        "Ask a question about your uploaded medical report..."
    )

    if not prompt:
        return

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    headers = {
        "Authorization": f"Bearer {st.session_state.token}"
    }

    response = requests.post(
        f"{BACKEND_URL}/api/v1/medical/consult",
        headers=headers,
        json={
            "query": prompt
        }
    )

    if response.status_code == 200:

        answer = response.json()["response"]

    else:

        answer = response.text

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)