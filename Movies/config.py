import os
PORT=int(os.getenv("PORT",5000))
CHATBOT_TITLE="Movies"
DOMAIN="Movie Guide"
SYSTEM_PROMPT="You are a Movie Guide assistant. Answer ONLY Movie Guide questions and politely refuse unrelated questions."
WELCOME_MESSAGE="Welcome to Movies."
THEME={"primary":"#0ea5e9","bg":"#08131b","style":"cinema"}
