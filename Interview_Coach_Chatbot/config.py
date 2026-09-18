
import os
CHATBOT_TITLE="Interview Coach Chatbot"
DOMAIN="Interview Preparation"
WELCOME_MESSAGE="Welcome to Interview Coach Chatbot."
SYSTEM_PROMPT=f"""You are {CHATBOT_TITLE}.
Answer ONLY questions related to {DOMAIN}.
Politely refuse unrelated questions."""
PRIMARY_COLOR="#EF4444"
MODEL_NAME=os.getenv("MODEL_NAME","gemini-2.5-flash-lite")
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY","PASTE_API_KEY_HERE")
PORT=int(os.getenv("PORT",5000))
SECRET_KEY=os.getenv("SECRET_KEY","change-this-secret")
