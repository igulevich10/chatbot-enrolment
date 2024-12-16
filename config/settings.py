import os
from dotenv import load_dotenv

# Завантажуємо змінні з .env
load_dotenv()

# Ключі для Telegram та OpenAI
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Інші налаштування
BOT_USERNAME = "enrolment1_bot"
LOG_FILE = "app/logs/bot.log"

