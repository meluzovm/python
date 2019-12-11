import logging
import sys
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

#Enable Logging 
#logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO, filename='bot.log')
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


#Functions 

#deprecated 
#def start(bot, update):
#    """Send a message when the command /start is issued."""
#    logger.info("/start is issued")
#    update.message.reply_text('Hi!')

def cmd_start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    logger.info("/start is issued")
    update.message.reply_text('Hi!')

def cmd_exit(update: Update, context: CallbackContext):
    """Stop bot """
    logger.info("/exit is issued")
    update.message.reply_text('Bye!')
    sys.exit(1)

def answer(update: Update, context: CallbackContext):
    """Send a response to message."""
    logger.info("Message recieved")
    user_text = update.message.text
    print(update.message)
    print(user_text)
    update.message.reply_text(user_text)
  
# Content of update.message  
"""
{'message_id': 46, 'date': 1575464224, 'chat': {'id': 29055811, 'type': 'private', 'username': 'meluzovm', 'first_name': 'Mikhail', 'last_name': 'Meluzov'}, 'text': '111', 'entities': [], 'caption_entities': [], 'photo': [], 'new_chat_members': [], 'new_chat_photo': [], 'delete_chat_photo': False, 'group_chat_created': False, 'supergroup_chat_created': False, 'channel_chat_created': False, 'from': {'id': 29055811, 'first_name': 'Mikhail', 'is_bot': False, 'last_name': 'Meluzov', 'username': 'meluzovm', 'language_code': 'en'}}
"""

def main():
    #deprecated
    #bot = Updater("513285340:AAFouumHDKKq-xXj59_qbaXzlsVZ3tPHh7E")
    bot = Updater('513285340:AAFouumHDKKq-xXj59_qbaXzlsVZ3tPHh7E', use_context=True)
    
    logger.info("Bot staring")

    dp = bot.dispatcher
    dp.add_handler(CommandHandler("start", cmd_start))
    dp.add_handler(CommandHandler("exit", cmd_exit))
    dp.add_handler(MessageHandler(Filters.text, answer))

    bot.start_polling()
    bot.idle()


#MAIN 
main()

