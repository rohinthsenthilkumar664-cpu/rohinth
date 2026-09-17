# Finance Assistant

Domain-specific Flask + Gemini chatbot.

## Features
- No login or registration
- Temporary Flask session chat history
- Domain-restricted system prompt
- Responsive single-page UI
- Configurable settings in `config.py`
- Gunicorn/Render compatible

## Configuration
Set `GEMINI_API_KEY` in `.env`. Change the chatbot title, domain, prompt, welcome message, and port in `config.py`.

## Deployment
Use Gunicorn with:
`gunicorn app:app`

Set the Render environment variable `GEMINI_API_KEY` and use the PORT supplied by Render.

## Privacy note
The app uses a signed Flask session cookie by default. For production, use a strong `FLASK_SECRET_KEY`, HTTPS, and review cookie/session settings. Do not place confidential data in chat messages.
