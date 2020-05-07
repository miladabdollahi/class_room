import telebot, logging, os
from db import Base, engine
import config

logger = telebot.logger
logger.setLevel(logging.INFO)
bot = telebot.TeleBot(os.getenv('TOKEN'))
Base.metadata.create_all(engine)


def home_menu(message):
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    markup = telebot.types.ReplyKeyboardMarkup()
    list_of_books = telebot.types.KeyboardButton('لیست درس ها')
    about_me = telebot.types.KeyboardButton('درباره ما')
    if is_admin(message):
        manage_bot = telebot.types.KeyboardButton('مدیریت ربات')
        markup.add(manage_bot)
    markup.add(list_of_books)
    markup.add(about_me)
    bot.send_message(chat_id=message.chat.id, text='از منوی کنار استیکر کمک بگیرید!', reply_markup=markup)


def is_admin(message):
    if message.chat.username in config.Managers.usernames:
        return True
    return False


@bot.message_handler(commands=['start'])
def start(message):
    msg = 'سلام دانش اموز ' + message.chat.first_name + ' ' + message.chat.last_name + 'عزیز به ربات دانش یار خوش امدید .'
    bot.send_message(chat_id=message.chat.id, text=msg)
    home_menu(message)


bot.polling()
