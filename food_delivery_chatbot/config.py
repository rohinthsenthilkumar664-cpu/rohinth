import os

CHATBOT_TITLE = 'Food Delivery Chatbot'
DOMAIN = 'Food delivery and restaurants'
SYSTEM_PROMPT = 'You are Food Delivery Chatbot, a helpful and respectful AI assistant focused only on Food delivery and restaurants. Provide clear, practical, domain-related answers. Refuse unrelated requests politely. For high-risk topics, encourage professional help and avoid pretending to be an expert.'
WELCOME_MESSAGE = 'Welcome to Food Delivery Chatbot! Ask me anything related to Food delivery and restaurants.'
MAX_HISTORY = int(os.getenv("MAX_HISTORY", "12"))
PORT = int(os.getenv("PORT", "10000"))
