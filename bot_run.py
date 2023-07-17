from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

# import handlers
from weather import handlers


TOKEN = os.environ.get('TOKEN')

def main() -> None:
    # updater
    updater = Updater(TOKEN)

    # dispatcher
    dispatcher = updater.dispatcher

    # handlers
    dispatcher.add_handler(CommandHandler('start', handlers.start))
    

    # start polling
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()