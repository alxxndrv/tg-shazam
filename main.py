from telegram.ext import CommandHandler
import logging
import texts
from telegram.ext import Updater
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.
token = os.getenv("TELEGRAM_BOT_TOKEN")
assert token is not None

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=texts.welcome_text)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
