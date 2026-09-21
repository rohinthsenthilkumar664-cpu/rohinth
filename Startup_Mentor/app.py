from flask import Flask, render_template, request, session
import os
from config import CONFIG
app = Flask(__name__)
app.secret_key=os.getenv("SECRET_KEY","dev-key")
@app.route("/", methods=["GET","POST"])
def index():
    if "history" not in session: session["history"]=[]
    if request.method=="POST":
        q=request.form["message"]
        session["history"].append({"role":"user","text":q})
        session["history"].append({"role":"bot","text":"Gemini API integration placeholder. Answer only in configured domain."})
        session.modified=True
    return render_template("index.html", config=CONFIG, history=session["history"])
if __name__=="__main__":
    app.run(host="0.0.0.0", port=CONFIG["PORT"], debug=True)
