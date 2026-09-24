
CHATBOT_TITLE="Recipe Assistant"
DOMAIN="Cooking"
SYSTEM_PROMPT="""You are Recipe Assistant. Answer ONLY questions related to Cooking. Politely refuse unrelated questions."""
WELCOME_MESSAGE="Welcome to Recipe Assistant!"
THEME={"primary":"#F59E0B"}
LAYOUT="card"
PORT=int(__import__("os").getenv("PORT","5000"))
