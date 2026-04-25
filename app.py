# from flask import Flask,request,jsonify
# from flask_cors import CORS
# import os
# from dotenv import load_dotenv
# from langchain.memory import ConversationBufferMemory
# #from langchain.memory import ConversationBufferMemory
# #from langchain.memory import ConversationBufferMemory
# from langchain_google_genai import ChatGoogleGenerativeAI

# #load Env
# load_dotenv()
# GOOGLE_GEMINI_API_KEY=os.getenv("GOOGLE_GEMINI_API_KEY")

# if not GOOGLE_GEMINI_API_KEY:
#     raise ValueError("API_KEY is not sen in .env")

# #initialize flask app
# app=Flask(__name__)
# CORS(app,resources={r"/chat" : {"origin":"*"}})

# #initialize langchain components
# memory=ConversationalBufferMemory(memory_keys="chat_history",return_message=True)
# gemini_chat=ChatGoogleGenerativeAI(model="gemin-1.5-flash",api_key=GOOGLE_GEMINI_API_KEY)

# #create route

# @app.route("/chat",method=["POST"])
# def chat():
#     data=request.get_json()
#     message=data.get("message")

#     if not message:
#         return jsonify({"error":"Message is required"}),400
    
#     try:
#         chat_history=memory.chat_memory.messages

#         response=gemini_chat.invoke(message)

#         bot_reply=response.content

#         memory.sav_context({"input":message},{"output":bot_reply})

#         return jsonify({"reply":bot_reply})
    
#     except Exception as e:
#         print("Error:",str(e))
#         return jsonify({"error":"Failed to fetch response"}),500


# if __name__=="__main__":
#     app.run(port=5000,debug=True)
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from langchain.memory import ConversationBufferMemory  # ✅ SAME RAKHA
from langchain_google_genai import ChatGoogleGenerativeAI  # ✅ SAME RAKHA

load_dotenv()
GOOGLE_GEMINI_API_KEY = os.getenv("GOOGLE_GEMINI_API_KEY")

if not GOOGLE_GEMINI_API_KEY:
    raise ValueError("API_KEY is not set in .env")

app = Flask(__name__)
CORS(app, resources={r"/chat": {"origins": "*"}})  # FIXED: "origin" → "origins"


memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
gemini_chat = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=GOOGLE_GEMINI_API_KEY)  # FIXED: "gemin" → "gemini"


SYSTEM_PROMPT = """You are EduBot, a friendly AI Study Assistant for college students.
Your job is to:
- Explain concepts in simple, easy to understand language
- Give exam tips and tricks
- Solve doubts in subjects like Python, DSA, ML, DBMS, OOPs
- Give short summaries and bullet points when explaining topics
- Encourage students and keep them motivated
Always respond in a clear, student-friendly tone."""

@app.route("/chat", methods=["POST"])  # FIXED: "method" → "methods"
def chat():
    data = request.get_json()
    message = data.get("message")

    if not message:
        return jsonify({"error": "Message is required"}), 400

    try:
        chat_history = memory.chat_memory.messages
        full_message = f"{SYSTEM_PROMPT}\n\nStudent question: {message}"
        response = gemini_chat.invoke(full_message)
        bot_reply = response.content
        memory.save_context({"input": message}, {"output": bot_reply})
        return jsonify({"reply": bot_reply})

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": "Failed to fetch response"}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True)