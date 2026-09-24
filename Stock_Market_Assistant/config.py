
CHATBOT_TITLE="Stock Market Assistant"
DOMAIN="Indian Stock Market"
SYSTEM_PROMPT="""You are Stock Market Assistant. Answer ONLY questions related to Indian Stock Market. Politely refuse unrelated questions."""
WELCOME_MESSAGE="Welcome to Stock Market Assistant!"
THEME={"primary":"#22C55E"}
LAYOUT="terminal"
PORT=int(__import__("os").getenv("PORT","5000"))
