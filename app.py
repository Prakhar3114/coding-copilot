# app.py
import streamlit as st
from backend import ask_llama
from PIL import Image

# --- App Settings ---
st.set_page_config(
    page_title="Coding Copilot",
    page_icon="🤖",
    layout="wide"
)

# --- Load Logo ---
logo_path = "assets/logo.png"  # Replace with your logo path
st.markdown(
    """
    <div style='display: flex; align-items: center;'>
        <img src='assets/logo.png' width='50' style='margin-right:10px'>
        <h2 style='color: #f3f3f3;'>Coding Copilot</h2>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# --- Initialize Session State ---
if "messages" not in st.session_state:
    st.session_state.messages = []

if "task_type" not in st.session_state:
    st.session_state.task_type = "default"

# --- Sidebar Options ---
with st.sidebar:
    st.title("⚙️ Options")
    st.markdown("### What do you want to do?")
    if st.button("🛠️ Generate Code"):
        st.session_state.task_type = "generate"
    if st.button("📖 Explain Code"):
        st.session_state.task_type = "explain"
    if st.button("🐞 Debug Code"):
        st.session_state.task_type = "debug"
    if st.button("🔄 Reset"):
        st.session_state.messages = []
        st.session_state.task_type = "default"

st.markdown("---")
st.subheader("📁 Upload Code File")

uploaded_file = st.file_uploader("Choose a Python (.py) or text (.txt) file", type=["py", "txt"])

if uploaded_file:
    file_content = uploaded_file.read().decode("utf-8")
    st.code(file_content, language="python")

    if st.button("Analyze File"):
        with st.spinner("Analyzing file with AI Copilot..."):
            response = ask_llama(file_content, task_type)
            st.markdown("### 🤖 Copilot's Response:")
            st.markdown(response)

# --- Display Chat History ---
for msg in st.session_state.messages:
    role = "👤 You" if msg["role"] == "user" else "🤖 Copilot"
    st.markdown(f"**{role}:**")
    st.markdown(msg["content"], unsafe_allow_html=True)

# --- Input Box ---
user_input = st.chat_input("Type your prompt here...")

if user_input:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get assistant response
    with st.spinner("Thinking..."):
        assistant_response = ask_llama(user_input, st.session_state.task_type)
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
        st.markdown("**🤖 Copilot:**")
        st.markdown(assistant_response, unsafe_allow_html=True)
