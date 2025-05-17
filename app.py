# app.py
import streamlit as st
from backend import ask_llama

st.set_page_config(page_title="Coding Copilot", page_icon="🤖")
st.title("🤖 Coding Copilot")
st.caption("Powered by LLaMA 3 (Groq API)")

# Store conversation
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

# Chat input
prompt = st.chat_input("Ask me a coding question...")

if prompt:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    # Get response from LLM
    response = ask_llama(prompt)

    # Add assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").markdown(response)
