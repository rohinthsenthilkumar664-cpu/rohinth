
CHATBOT_TITLE="Movie Recommendation"
DOMAIN="Movies"
SYSTEM_PROMPT="""You are Movie Recommendation. Answer ONLY questions related to Movies. Politely refuse unrelated questions."""
WELCOME_MESSAGE="Welcome to Movie Recommendation!"
THEME={"primary":"#111827"}
LAYOUT="terminal"
PORT=int(__import__("os").getenv("PORT","5000"))
