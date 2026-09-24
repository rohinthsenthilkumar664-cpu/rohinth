
CHATBOT_TITLE="Fitness Coach"
DOMAIN="Fitness"
SYSTEM_PROMPT="""You are Fitness Coach. Answer ONLY questions related to Fitness. Politely refuse unrelated questions."""
WELCOME_MESSAGE="Welcome to Fitness Coach!"
THEME={"primary":"#F97316"}
LAYOUT="glass"
PORT=int(__import__("os").getenv("PORT","5000"))
