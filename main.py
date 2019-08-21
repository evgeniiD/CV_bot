
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import logging
from cv_bot import handlers, mytoken

TOKEN = mytoken.TOKEN
updater = Updater(token=TOKEN, use_context=True)

dispatcher = updater.dispatcher


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# the very start
start_handler = CommandHandler('start', handlers.start)
dispatcher.add_handler(start_handler)
#1st button
updater.dispatcher.add_handler(CallbackQueryHandler(handlers.button_for_start_bio, pattern='start bio'))
#2nd button

updater.dispatcher.add_handler(CallbackQueryHandler(handlers.button_to_calm_down, pattern='^calm_down$'))

updater.dispatcher.add_handler(CallbackQueryHandler(handlers.about_front, pattern='^front$'))

updater.start_polling()