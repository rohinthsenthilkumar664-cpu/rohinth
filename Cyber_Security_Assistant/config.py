
CHATBOT_TITLE="Cyber Security Assistant"
DOMAIN="Cyber Security"
SYSTEM_PROMPT="""You are Cyber Security Assistant. Answer ONLY questions related to Cyber Security. Politely refuse unrelated questions."""
WELCOME_MESSAGE="Welcome to Cyber Security Assistant!"
THEME={"primary":"#0F172A"}
LAYOUT="neon"
PORT=int(__import__("os").getenv("PORT","5000"))
