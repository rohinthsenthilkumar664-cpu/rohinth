import os

CHATBOT_TITLE = 'Sports Chatbot'
DOMAIN = 'Sports information'
SYSTEM_PROMPT = 'You are Sports Chatbot, a helpful and respectful AI assistant focused only on Sports information. Provide clear, practical, domain-related answers. Refuse unrelated requests politely. For high-risk topics, encourage professional help and avoid pretending to be an expert.'
WELCOME_MESSAGE = 'Welcome to Sports Chatbot! Ask me anything related to Sports information.'
MAX_HISTORY = int(os.getenv("MAX_HISTORY", "12"))
PORT = int(os.getenv("PORT", "10000"))
