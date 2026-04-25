# 🎓 EduBot — AI Study Assistant Chatbot

An AI-powered full-stack chatbot designed to help students with doubt solving, concept explanations, and exam preparation — built using Google Gemini API, LangChain, Flask, and React.js.

---

## 🚀 Features

- 💬 **Conversational AI** — Ask any academic doubt and get clear, student-friendly answers
- 🧠 **Memory** — Remembers previous messages in the conversation using LangChain
- 📚 **Domain-Specific** — Tuned via prompt engineering to act as a study tutor
- ⚡ **Real-time Responses** — Fast replies powered by Google Gemini 1.5 Flash
- 🌐 **Full-Stack** — React.js frontend + Python Flask backend

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React.js, Axios |
| Backend | Python, Flask, Flask-CORS |
| AI/LLM | Google Gemini API (gemini-1.5-flash) |
| Memory | LangChain ConversationBufferMemory |
| Prompt Engineering | System-level prompt for study assistant role |

---

## 📁 Project Structure

```
chatbot/
├── app.py                  # Flask backend with Gemini + LangChain
├── .env                    # API key (not committed)
├── requirements.txt        # Python dependencies
└── frontend/
    └── src/
        ├── App.jsx         # React chat UI
        └── App.css         # Styling
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/edubot-ai-study-assistant
cd edubot-ai-study-assistant
```

### 2. Backend Setup
```bash
# Create virtual environment
python -m venv chatbot_env
chatbot_env\Scripts\activate      # Windows
# source chatbot_env/bin/activate  # Mac/Linux

# Install dependencies
pip install flask flask-cors python-dotenv langchain==0.1.20 langchain-google-genai
```

### 3. Add API Key
Create a `.env` file in the root folder:
```
GOOGLE_GEMINI_API_KEY=your_api_key_here
```
Get your free API key at: https://aistudio.google.com

### 4. Frontend Setup
```bash
cd frontend
npm install
npm install axios
```

---

## ▶️ Run the App

Open **two terminals**:

**Terminal 1 — Backend:**
```bash
chatbot_env\Scripts\activate
python app.py
```

**Terminal 2 — Frontend:**
```bash
cd frontend
npm run dev
```

Open browser: **http://localhost:5173/**

---



