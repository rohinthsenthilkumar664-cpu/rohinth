
from flask import Flask, render_template, request, jsonify, session
from dotenv import load_dotenv
import google.generativeai as genai
import os
from config import *

load_dotenv()
app=Flask(__name__)
app.secret_key=SECRET_KEY
genai.configure(api_key=os.getenv("GEMINI_API_KEY", GEMINI_API_KEY))
model=genai.GenerativeModel(MODEL_NAME)

@app.get("/")
def home():
    session.setdefault("history",[])
    return render_template("index.html", title=CHATBOT_TITLE, welcome=WELCOME_MESSAGE, color=PRIMARY_COLOR)

@app.post("/chat")
def chat():
    msg=request.json.get("message","")
    prompt=f"{SYSTEM_PROMPT}\nUser: {msg}"
    try:
        reply=model.generate_content(prompt).text
    except Exception as e:
        reply=f"Error: {e}"
    return jsonify({"reply":reply})

if __name__=="__main__":
    app.run(host="0.0.0.0", port=PORT)
