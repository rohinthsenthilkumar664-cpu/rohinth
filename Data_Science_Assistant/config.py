
CHATBOT_TITLE="Data Science Assistant"
DOMAIN="Data Science"
SYSTEM_PROMPT="""You are Data Science Assistant. Answer ONLY questions related to Data Science. Politely refuse unrelated questions."""
WELCOME_MESSAGE="Welcome to Data Science Assistant!"
THEME={"primary":"#2563EB"}
LAYOUT="glass"
PORT=int(__import__("os").getenv("PORT","5000"))
