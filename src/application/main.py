"""Simple Bot for get weather current in Saint-Petersburg."""
import logging
import os

from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
)

from weather_utils import create_weather_message

PORT = int(os.environ.get('PORT', 8443))

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = os.environ["TOKEN"]


def start(update, context) -> None:
    """Send a message when the command /start is issued."""
    weather = create_weather_message()
    update.message.reply_text(weather)


def help_command(update, context) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(update, context) -> None:
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main() -> None:
    updater = Updater(TOKEN, use_context=True)

    # Dispatcher to register handlers
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, echo))

    # Log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_webhook(
        listen="0.0.0.0",
        port=int(PORT),
        url_path=TOKEN,
        webhook_url='https://weather-spb-telegram-bot.herokuapp.com/' + TOKEN,
    )

    # Run the bot
    updater.idle()


if __name__ == '__main__':
    main()
