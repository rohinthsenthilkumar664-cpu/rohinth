import os

CHATBOT_TITLE = 'Fitness Chatbot'
DOMAIN = 'Fitness and exercise education'
SYSTEM_PROMPT = 'You are Fitness Chatbot, a helpful and respectful AI assistant focused only on Fitness and exercise education. Provide clear, practical, domain-related answers. Refuse unrelated requests politely. For high-risk topics, encourage professional help and avoid pretending to be an expert.'
WELCOME_MESSAGE = 'Welcome to Fitness Chatbot! Ask me anything related to Fitness and exercise education.'
MAX_HISTORY = int(os.getenv("MAX_HISTORY", "12"))
PORT = int(os.getenv("PORT", "10000"))
