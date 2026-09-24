
CHATBOT_TITLE="Crypto Assistant"
DOMAIN="Cryptocurrency"
SYSTEM_PROMPT="""You are Crypto Assistant. Answer ONLY questions related to Cryptocurrency. Politely refuse unrelated questions."""
WELCOME_MESSAGE="Welcome to Crypto Assistant!"
THEME={"primary":"#8B5CF6"}
LAYOUT="neon"
PORT=int(__import__("os").getenv("PORT","5000"))
