
CHATBOT_TITLE="Travel Guide Assistant"
DOMAIN="Travel"
SYSTEM_PROMPT="""You are Travel Guide Assistant. Answer ONLY questions related to Travel. Politely refuse unrelated questions."""
WELCOME_MESSAGE="Welcome to Travel Guide Assistant!"
THEME={"primary":"#0EA5E9"}
LAYOUT="glass"
PORT=int(__import__("os").getenv("PORT","5000"))
