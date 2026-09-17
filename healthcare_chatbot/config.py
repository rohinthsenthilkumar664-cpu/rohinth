import os

CHATBOT_TITLE = 'Healthcare Chatbot'
DOMAIN = 'General health education'
SYSTEM_PROMPT = 'You are Healthcare Chatbot, a helpful and respectful AI assistant focused only on General health education. Provide clear, practical, domain-related answers. Refuse unrelated requests politely. For high-risk topics, encourage professional help and avoid pretending to be an expert.'
WELCOME_MESSAGE = 'Welcome to Healthcare Chatbot! Ask me anything related to General health education.'
MAX_HISTORY = int(os.getenv("MAX_HISTORY", "12"))
PORT = int(os.getenv("PORT", "10000"))
