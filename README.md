# 🤖 Coding Copilot Chatbot

A Streamlit-powered AI coding assistant built using **Groq API** and **LLaMA-3** models.  
Supports multiple tasks including code generation, explanation, debugging, and file-based analysis.

![Logo](assets/logo.png)

---

## 🚀 Features

- ✅ **Chat-based coding assistant**
- 🛠️ Task modes: **Generate**, **Explain**, **Debug**
- 📁 Upload `.py` or `.txt` files for analysis
- 🌙 **Custom UI** with dark theme and your branding
- 💬 Markdown + code block formatting
- 🔐 API key managed securely using `.env` + Streamlit secrets
- ☁️ Deployed via [Streamlit Cloud](https://streamlit.io/cloud)

---

## 📂 Project Structure

coding-assistant-chatbot/
├── app.py # Streamlit frontend UI
├── backend.py # Groq API logic and task handling
├── requirements.txt # Dependencies for deployment
├── .env # Local API key storage (not pushed)
├── assets/
│ └── logo.png # Your profile/logo image

yaml
Copy
Edit

---

## ⚙️ Setup Locally

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/coding-copilot.git
cd coding-copilot
2. Create a virtual environment
bash
Copy
Edit
python -m venv .venv
.venv\Scripts\activate    # Windows
# source .venv/bin/activate  # macOS/Linux
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Add your Groq API key to a .env file
ini
Copy
Edit
GROQ_API_KEY=your-api-key-here
🧠 How It Works
This assistant uses the Groq API with LLaMA 3 models (8B or 70B) to understand and respond to your coding prompts.
Each task type sends a specific system message to guide the LLM behavior:

Generate: Produces new code based on user input

Explain: Explains code or concepts

Debug: Fixes buggy code

Uploaded files are automatically read and analyzed based on your selected task.

🌐 Deployment
Streamlit Cloud Setup
Push this repo to GitHub

Go to streamlit.io/cloud

Click "New App"

Set:

Repository: your-username/coding-copilot

Branch: main

Main file: app.py

Add your API key in the "Secrets" section:

ini
Copy
Edit
GROQ_API_KEY=your-api-key-here
Click Deploy 🚀

📸 Demo Screenshot
(Add a screenshot here by uploading and linking if you want)

📌 To-Do / Future Enhancements
 Add support for more file types (e.g., .js, .cpp)

 Allow download of debugged/fixed code

 Add prompt templates and quick examples

 Multi-language code toggle

🧑‍💻 Author
Prakhar
Built with ❤️ using Python, Streamlit, Groq, and LLaMA-3.

📝 License
MIT License — use freely, give credit if helpful!

yaml
Copy
Edit

---

Just replace `YOUR_USERNAME` and `your-api-key-here` with your actual GitHub username and Groq API key instructions.

Let me know if you want me to add badges or contribution guidelines!







