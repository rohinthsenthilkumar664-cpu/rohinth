
CHATBOT_TITLE="Farmer Assistant"
DOMAIN="Agriculture"
SYSTEM_PROMPT="""You are Farmer Assistant. Answer ONLY questions related to Agriculture. Politely refuse unrelated questions."""
WELCOME_MESSAGE="Welcome to Farmer Assistant!"
THEME={"primary":"#15803D"}
LAYOUT="card"
PORT=int(__import__("os").getenv("PORT","5000"))
