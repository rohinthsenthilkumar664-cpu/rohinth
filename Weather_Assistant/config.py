
CHATBOT_TITLE="Weather Assistant"
DOMAIN="Weather"
SYSTEM_PROMPT="""You are Weather Assistant. Answer ONLY questions related to Weather. Politely refuse unrelated questions."""
WELCOME_MESSAGE="Welcome to Weather Assistant!"
THEME={"primary":"#38BDF8"}
LAYOUT="glass"
PORT=int(__import__("os").getenv("PORT","5000"))
