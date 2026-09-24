
CHATBOT_TITLE="JEE Assistant"
DOMAIN="JEE Prep"
SYSTEM_PROMPT="""You are JEE Assistant. Answer ONLY questions related to JEE Prep. Politely refuse unrelated questions."""
WELCOME_MESSAGE="Welcome to JEE Assistant!"
THEME={"primary":"#EA580C"}
LAYOUT="card"
PORT=int(__import__("os").getenv("PORT","5000"))
