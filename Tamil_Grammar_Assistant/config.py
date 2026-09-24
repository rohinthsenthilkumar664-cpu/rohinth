
CHATBOT_TITLE="Tamil Grammar Assistant"
DOMAIN="Tamil Grammar"
SYSTEM_PROMPT="""You are Tamil Grammar Assistant. Answer ONLY questions related to Tamil Grammar. Politely refuse unrelated questions."""
WELCOME_MESSAGE="Welcome to Tamil Grammar Assistant!"
THEME={"primary":"#991B1B"}
LAYOUT="clean"
PORT=int(__import__("os").getenv("PORT","5000"))
