
from flask import Flask,render_template,request,jsonify,session
from dotenv import load_dotenv
from google import genai
import os,config
load_dotenv()
app=Flask(__name__); app.secret_key=os.getenv("SECRET_KEY","secret")
client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
@app.get("/")
def home(): return render_template("index.html",cfg=config)
@app.post("/chat")
def chat():
 m=(request.json or {}).get("message","").strip()
 if not m:return jsonify(reply="Enter a message"),400
 session.setdefault("history",[])
 try:r=client.models.generate_content(model="gemini-2.5-flash-lite",contents=f"{config.SYSTEM_PROMPT}\nUser:{m}").text
 except Exception as e:r=f"Error: {e}"
 session["history"].append({"u":m,"a":r});session.modified=True
 return jsonify(reply=r)
@app.post("/clear")
def clear(): session.clear(); return jsonify(ok=True)
if __name__=="__main__": app.run(host="0.0.0.0",port=config.PORT)
