# app.py
import streamlit as st
from backend import ask_llama

# --- App Settings ---
st.set_page_config(
    page_title="Coding Copilot",
    page_icon="🤖",
    layout="wide"
)

# --- Custom CSS ---
st.markdown("""
    <style>
        body {
            background-color: #0f1117;
            color: #f3f3f3;
            font-family: 'Segoe UI', sans-serif;
        }
        .sidebar .sidebar-content {
            background-color: #1a1c23;
        }
        h2 {
            font-weight: 700;
        }
        .stButton > button {
            color: white;
            background-color: #202b3b;
            border: none;
            border-radius: 8px;
            padding: 0.5rem 1rem;
            margin-bottom: 8px;
            transition: all 0.3s ease;
        }
        .stButton > button:hover {
            background-color: #00b3ff;
            color: black;
        }
        .chat-bubble {
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 10px;
        }
        .user-bubble {
            background-color: #2c3e50;
            color: #fff;
        }
        .ai-bubble {
            background-color: #16a085;
            color: #fff;
        }
        .code-preview {
            background-color: #2d2d2d;
            border-radius: 10px;
            padding: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Header with Robot Icon and White Title ---
st.markdown("""
    <div style='display: flex; align-items: center; gap: 10px;'>
        <span style="font-size: 2.2rem;">🤖</span>
        <h2 style='margin: 0; color: white;'>Coding Copilot</h2>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- Session State ---
if "messages" not in st.session_state:
    st.session_state.messages = []

if "task_type" not in st.session_state:
    st.session_state.task_type = "default"

# --- Sidebar ---
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

# --- File Upload ---
st.markdown("---")
st.subheader("📁 Upload Code File")

uploaded_file = st.file_uploader("Choose a Python (.py) or text (.txt) file", type=["py", "txt"])

if uploaded_file:
    file_content = uploaded_file.read().decode("utf-8")
    st.markdown("<div class='code-preview'>", unsafe_allow_html=True)
    st.code(file_content, language="python")
    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("Analyze File"):
        with st.spinner("Analyzing file with AI Copilot..."):
            response = ask_llama(file_content, st.session_state.task_type)
            st.markdown("### 🤖 Copilot's Response:")
            st.markdown(f"<div class='chat-bubble ai-bubble'>{response}</div>", unsafe_allow_html=True)

# --- Chat History ---
for msg in st.session_state.messages:
    role = msg["role"]
    bubble_class = "user-bubble" if role == "user" else "ai-bubble"
    name = "👤 You" if role == "user" else "🤖 Copilot"
    st.markdown(f"**{name}:**")
    st.markdown(f"<div class='chat-bubble {bubble_class}'>{msg['content']}</div>", unsafe_allow_html=True)

# --- Chat Input ---
user_input = st.chat_input("Type your prompt here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.spinner("Thinking..."):
        response = ask_llama(user_input, st.session_state.task_type)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.markdown("**🤖 Copilot:**")
        st.markdown(f"<div class='chat-bubble ai-bubble'>{response}</div>", unsafe_allow_html=True)
