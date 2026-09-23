import os
PORT=int(os.getenv("PORT",5000))
CHATBOT_TITLE="Recipes"
DOMAIN="Recipes"
SYSTEM_PROMPT="You are a Recipes assistant. Answer ONLY Recipes questions and politely refuse unrelated questions."
WELCOME_MESSAGE="Welcome to Recipes."
THEME={"primary":"#2563eb","bg":"#0f172a","style":"kitchen"}
