
CHATBOT_TITLE="Medical Information Assistant"
DOMAIN="Medical Info"
SYSTEM_PROMPT="""You are Medical Information Assistant. Answer ONLY questions related to Medical Info. Politely refuse unrelated questions."""
WELCOME_MESSAGE="Welcome to Medical Information Assistant!"
THEME={"primary":"#0284C7"}
LAYOUT="clean"
PORT=int(__import__("os").getenv("PORT","5000"))
