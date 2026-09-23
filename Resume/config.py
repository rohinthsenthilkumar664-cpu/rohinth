import os
PORT=int(os.getenv("PORT",5000))
CHATBOT_TITLE="Resume"
DOMAIN="Resume Builder"
SYSTEM_PROMPT="You are a Resume Builder assistant. Answer ONLY Resume Builder questions and politely refuse unrelated questions."
WELCOME_MESSAGE="Welcome to Resume."
THEME={"primary":"#0ea5e9","bg":"#08131b","style":"minimal-gray"}
