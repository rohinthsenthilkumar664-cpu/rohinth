
from flask import Flask, render_template, request, jsonify, session
import os
from config import *
from google import genai
app=Flask(__name__)
app.secret_key=os.getenv("SECRET_KEY","change-me")
client=genai.Client(api_key=os.getenv("GEMINI_API_KEY",""))
@app.route("/")
def home():
    session.setdefault("history",[])
    return render_template("index.html",title=CHATBOT_TITLE,welcome=WELCOME_MESSAGE,theme=THEME,layout=LAYOUT)
@app.route("/chat",methods=["POST"])
def chat():
    msg=request.json.get("message","")
    if not msg:return jsonify({"reply":"Please enter a message."})
    prompt=f"{SYSTEM_PROMPT}\nUser:{msg}"
    try:
        r=client.models.generate_content(model="gemini-2.5-flash-lite",contents=prompt)
        reply=r.text
    except Exception:
        reply="Gemini API key missing or unavailable."
    session["history"]=session.get("history",[])+[{"u":msg,"b":reply}]
    return jsonify({"reply":reply})
if __name__=="__main__":
    app.run(host="0.0.0.0",port=PORT)
