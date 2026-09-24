
CHATBOT_TITLE="English Speaking Assistant"
DOMAIN="Spoken English"
SYSTEM_PROMPT="""You are English Speaking Assistant. Answer ONLY questions related to Spoken English. Politely refuse unrelated questions."""
WELCOME_MESSAGE="Welcome to English Speaking Assistant!"
THEME={"primary":"#0EA5E9"}
LAYOUT="card"
PORT=int(__import__("os").getenv("PORT","5000"))
