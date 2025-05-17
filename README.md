---

# 🤖 Coding Copilot Chatbot

A Streamlit-powered AI coding assistant built using **Groq API** and **LLaMA-3** models.  
Supports multiple tasks including code generation, explanation, debugging, and file-based analysis.

---

## 🚀 Features

- ✅ Chat-based coding assistant  
- 🛠️ Task modes: **Generate**, **Explain**, **Debug**  
- 📁 Upload `.py` or `.txt` files for analysis  
- 🌙 Dark mode with your profile-based branding  
- 💬 Markdown + syntax highlighted code blocks  
- 🔐 Secure Groq API key via `.env` and Streamlit secrets  
- ☁️ 1-click deployment via Streamlit Cloud  

---

## 📂 Project Structure

```

coding-assistant-chatbot/
├── app.py               # Streamlit UI logic
├── backend.py           # Task selection & Groq API handling
├── requirements.txt     # Python dependencies
├── .env                 # Stores API key locally (not pushed)
├── assets/
│   └── logo.png         # Your profile picture as logo

````

---


### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/coding-copilot.git
cd coding-copilot
````

### 2. Set up a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate   # On Windows
# source .venv/bin/activate   # On macOS/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Groq API key to `.env`

Create a file named `.env` in the root folder:

```
GROQ_API_KEY=your-api-key-here
```

---

## 🧠 How It Works

The chatbot interacts with the Groq API using Meta's LLaMA 3 models (8B/70B), enabling:

* **Generate** → Produces new code based on natural language
* **Explain** → Explains any code snippet or file
* **Debug** → Finds and fixes errors in broken code

Uploaded files are automatically parsed and analyzed based on your selected task.

---

## 🌐 Deploy to Streamlit Cloud

1. Push this repo to your GitHub account
2. Visit: [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Click **"New app"**, then enter:

```
Repository: your-username/coding-copilot
Branch: main
Main file path: app.py
```

4. Click **"Advanced settings"** → Add this under **Secrets**:

```
GROQ_API_KEY=your-api-key-here
```

5. Click **Deploy** 🚀
   Your chatbot will be live at a public `.streamlit.app` URL!

---

## Deployed Link

https://prakhargarg-coding-copilot.streamlit.app

---

## ✅ To-Do / Improvements

* [ ] Add multi-language support (.js, .cpp, etc.)
* [ ] Include "Download Code" option
* [ ] Add prompt templates for faster interaction
* [ ] Allow user to select Groq model (8B / 70B)

---

## 👨‍💻 Author

**Prakhar**
Built with ❤️ using Python, Streamlit, Groq API, and Meta LLaMA 3.

---

## 📝 License

MIT License — open-source and free to use. Give credit if helpful!

```

