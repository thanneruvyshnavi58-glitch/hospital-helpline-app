import streamlit as st
from ai.chatbot import generate_helpline_response

st.title("💬 AI Medical & Helpline Assistant")
st.write("Ask questions about departments, schedules, services, or general guidance.")

# Track conversation sessions natively
if "messages" not in st.session_state:
    st.session_state.messages = []

# Output active content history loops
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User Chat Input Event Hooks
if prompt := st.chat_input("How can I assist you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Typing..."):
            response = generate_helpline_response(prompt)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
