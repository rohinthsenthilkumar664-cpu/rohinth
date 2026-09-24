
CHATBOT_TITLE="AI Prompt Assistant"
DOMAIN="Prompt Engineering"
SYSTEM_PROMPT="""You are AI Prompt Assistant. Answer ONLY questions related to Prompt Engineering. Politely refuse unrelated questions."""
WELCOME_MESSAGE="Welcome to AI Prompt Assistant!"
THEME={"primary":"#7C3AED"}
LAYOUT="neon"
PORT=int(__import__("os").getenv("PORT","5000"))
