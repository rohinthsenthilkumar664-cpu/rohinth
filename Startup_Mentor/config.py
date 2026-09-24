
CHATBOT_TITLE="Startup Mentor"
DOMAIN="Startups"
SYSTEM_PROMPT="""You are Startup Mentor. Answer ONLY questions related to Startups. Politely refuse unrelated questions."""
WELCOME_MESSAGE="Welcome to Startup Mentor!"
THEME={"primary":"#334155"}
LAYOUT="glass"
PORT=int(__import__("os").getenv("PORT","5000"))
