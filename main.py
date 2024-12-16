from telegram.ext import ApplicationBuilder
from config.settings import TELEGRAM_TOKEN
from app.handlers import commands, messages, buttons

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(commands.start_handler)
    app.add_handler(messages.message_handler)
    app.add_handler(buttons.button_handler)

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
