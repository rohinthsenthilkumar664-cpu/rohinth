
CHATBOT_TITLE="Weight Loss Coach"
DOMAIN="Weight Loss"
SYSTEM_PROMPT="""You are Weight Loss Coach. Answer ONLY questions related to Weight Loss. Politely refuse unrelated questions."""
WELCOME_MESSAGE="Welcome to Weight Loss Coach!"
THEME={"primary":"#10B981"}
LAYOUT="clean"
PORT=int(__import__("os").getenv("PORT","5000"))
