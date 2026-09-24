
CHATBOT_TITLE="UPSC Assistant"
DOMAIN="UPSC Exam"
SYSTEM_PROMPT="""You are UPSC Assistant. Answer ONLY questions related to UPSC Exam. Politely refuse unrelated questions."""
WELCOME_MESSAGE="Welcome to UPSC Assistant!"
THEME={"primary":"#1D4ED8"}
LAYOUT="glass"
PORT=int(__import__("os").getenv("PORT","5000"))
