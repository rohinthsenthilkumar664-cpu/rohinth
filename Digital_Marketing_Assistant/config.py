
CHATBOT_TITLE="Digital Marketing Assistant"
DOMAIN="Marketing"
SYSTEM_PROMPT="""You are Digital Marketing Assistant. Answer ONLY questions related to Marketing. Politely refuse unrelated questions."""
WELCOME_MESSAGE="Welcome to Digital Marketing Assistant!"
THEME={"primary":"#9333EA"}
LAYOUT="neon"
PORT=int(__import__("os").getenv("PORT","5000"))
