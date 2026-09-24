
CHATBOT_TITLE="Java Programming Assistant"
DOMAIN="Java"
SYSTEM_PROMPT="""You are Java Programming Assistant. Answer ONLY questions related to Java. Politely refuse unrelated questions."""
WELCOME_MESSAGE="Welcome to Java Programming Assistant!"
THEME={"primary":"#B91C1C"}
LAYOUT="terminal"
PORT=int(__import__("os").getenv("PORT","5000"))
