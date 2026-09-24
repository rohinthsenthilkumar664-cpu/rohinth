
CHATBOT_TITLE="Flask Developer Assistant"
DOMAIN="Flask Development"
SYSTEM_PROMPT="""You are Flask Developer Assistant. Answer ONLY questions related to Flask Development. Politely refuse unrelated questions."""
WELCOME_MESSAGE="Welcome to Flask Developer Assistant!"
THEME={"primary":"#2563EB"}
LAYOUT="terminal"
PORT=int(__import__("os").getenv("PORT","5000"))
