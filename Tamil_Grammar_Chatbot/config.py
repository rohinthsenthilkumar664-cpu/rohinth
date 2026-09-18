
import os
CHATBOT_TITLE="Tamil Grammar Chatbot"
DOMAIN="Tamil Grammar"
WELCOME_MESSAGE="Welcome to Tamil Grammar Chatbot."
SYSTEM_PROMPT=f"""You are {CHATBOT_TITLE}.
Answer ONLY questions related to {DOMAIN}.
Politely refuse unrelated questions."""
PRIMARY_COLOR="#9333EA"
MODEL_NAME=os.getenv("MODEL_NAME","gemini-2.5-flash-lite")
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY","PASTE_API_KEY_HERE")
PORT=int(os.getenv("PORT",5000))
SECRET_KEY=os.getenv("SECRET_KEY","change-this-secret")
