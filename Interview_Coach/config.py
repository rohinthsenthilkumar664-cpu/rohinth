
CHATBOT_TITLE="Interview Coach"
DOMAIN="Interview Practice"
SYSTEM_PROMPT="""You are Interview Coach. Answer ONLY questions related to Interview Practice. Politely refuse unrelated questions."""
WELCOME_MESSAGE="Welcome to Interview Coach!"
THEME={"primary":"#4F46E5"}
LAYOUT="glass"
PORT=int(__import__("os").getenv("PORT","5000"))
