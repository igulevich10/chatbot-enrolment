from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters
from app.services.chatgpt_service import chatgpt_response

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    ai_response = chatgpt_response(user_message)
    await update.message.reply_text(ai_response)

message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
