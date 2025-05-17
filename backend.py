# backend.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api.groq.com/openai/v1/chat/completions"
API_KEY = os.getenv("GROQ_API_KEY")

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

SYSTEM_PROMPTS = {
    "generate": "You are a helpful coding assistant. Generate code for the following request:",
    "explain": "You are a coding tutor. Explain the following code clearly:",
    "debug": "You are a code debugger. Fix the bugs or errors in the following code:",
    "default": "You are a helpful coding assistant. Answer the question below:"
}

def ask_llama(user_input, task_type="default"):
    system_message = SYSTEM_PROMPTS.get(task_type, SYSTEM_PROMPTS["default"])

    data = {
        "model": "llama3-8b-8192",  # or llama3-70b-8192
        "messages": [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.3
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=data)
        result = response.json()
        return result['choices'][0]['message']['content']
    except Exception as e:
        return f"❌ Error: {str(e)}"
