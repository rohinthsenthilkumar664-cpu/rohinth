
CHATBOT_TITLE="TNPSC Assistant"
DOMAIN="TNPSC Exam"
SYSTEM_PROMPT="""You are TNPSC Assistant. Answer ONLY questions related to TNPSC Exam. Politely refuse unrelated questions."""
WELCOME_MESSAGE="Welcome to TNPSC Assistant!"
THEME={"primary":"#16A34A"}
LAYOUT="clean"
PORT=int(__import__("os").getenv("PORT","5000"))
