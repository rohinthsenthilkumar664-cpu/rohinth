
CHATBOT_TITLE="Resume Builder Assistant"
DOMAIN="Resume Writing"
SYSTEM_PROMPT="""You are Resume Builder Assistant. Answer ONLY questions related to Resume Writing. Politely refuse unrelated questions."""
WELCOME_MESSAGE="Welcome to Resume Builder Assistant!"
THEME={"primary":"#64748B"}
LAYOUT="clean"
PORT=int(__import__("os").getenv("PORT","5000"))
