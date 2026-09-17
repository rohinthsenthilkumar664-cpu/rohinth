import os

CHATBOT_TITLE = 'Education Chatbot'
DOMAIN = 'Education and learning'
SYSTEM_PROMPT = 'You are Education Chatbot, a helpful and respectful AI assistant focused only on Education and learning. Provide clear, practical, domain-related answers. Refuse unrelated requests politely. For high-risk topics, encourage professional help and avoid pretending to be an expert.'
WELCOME_MESSAGE = 'Welcome to Education Chatbot! Ask me anything related to Education and learning.'
MAX_HISTORY = int(os.getenv("MAX_HISTORY", "12"))
PORT = int(os.getenv("PORT", "10000"))
