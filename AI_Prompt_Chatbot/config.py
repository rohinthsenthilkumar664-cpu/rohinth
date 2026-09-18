
import os
CHATBOT_TITLE="AI Prompt Chatbot"
DOMAIN="AI Prompt Engineering"
WELCOME_MESSAGE="Welcome to AI Prompt Chatbot."
SYSTEM_PROMPT=f"""You are {CHATBOT_TITLE}.
Answer ONLY questions related to {DOMAIN}.
Politely refuse unrelated questions."""
PRIMARY_COLOR="#8B5CF6"
MODEL_NAME=os.getenv("MODEL_NAME","gemini-2.5-flash-lite")
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY","PASTE_API_KEY_HERE")
PORT=int(os.getenv("PORT",5000))
SECRET_KEY=os.getenv("SECRET_KEY","change-this-secret")
