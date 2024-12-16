from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привіт! Я бот Херсонського державного університету. Як я можу допомогти?"
    )

start_handler = CommandHandler("start", start)
