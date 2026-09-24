
CHATBOT_TITLE="Real Estate Assistant"
DOMAIN="Real Estate"
SYSTEM_PROMPT="""You are Real Estate Assistant. Answer ONLY questions related to Real Estate. Politely refuse unrelated questions."""
WELCOME_MESSAGE="Welcome to Real Estate Assistant!"
THEME={"primary":"#A16207"}
LAYOUT="clean"
PORT=int(__import__("os").getenv("PORT","5000"))
