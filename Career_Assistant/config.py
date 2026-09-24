
CHATBOT_TITLE="Career Assistant"
DOMAIN="Career Guidance"
SYSTEM_PROMPT="""You are Career Assistant. Answer ONLY questions related to Career Guidance. Politely refuse unrelated questions."""
WELCOME_MESSAGE="Welcome to Career Assistant!"
THEME={"primary":"#2563EB"}
LAYOUT="glass"
PORT=int(__import__("os").getenv("PORT","5000"))
