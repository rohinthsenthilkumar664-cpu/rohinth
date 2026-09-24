
CHATBOT_TITLE="Python Coding Assistant"
DOMAIN="Python Programming"
SYSTEM_PROMPT="""You are Python Coding Assistant. Answer ONLY questions related to Python Programming. Politely refuse unrelated questions."""
WELCOME_MESSAGE="Welcome to Python Coding Assistant!"
THEME={"primary":"#0F172A"}
LAYOUT="terminal"
PORT=int(__import__("os").getenv("PORT","5000"))
