import os
PORT=int(os.getenv("PORT",5000))
CHATBOT_TITLE="Doctor"
DOMAIN="Medical Info"
SYSTEM_PROMPT="You are a Medical Info assistant. Answer ONLY Medical Info questions and politely refuse unrelated questions."
WELCOME_MESSAGE="Welcome to Doctor."
THEME={"primary":"#2563eb","bg":"#0f172a","style":"hospital"}
