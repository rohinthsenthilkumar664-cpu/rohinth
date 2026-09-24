
CHATBOT_TITLE="Personal Finance Assistant"
DOMAIN="Personal Finance"
SYSTEM_PROMPT="""You are Personal Finance Assistant. Answer ONLY questions related to Personal Finance. Politely refuse unrelated questions."""
WELCOME_MESSAGE="Welcome to Personal Finance Assistant!"
THEME={"primary":"#059669"}
LAYOUT="card"
PORT=int(__import__("os").getenv("PORT","5000"))
