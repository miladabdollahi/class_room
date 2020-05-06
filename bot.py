import telebot, logging, os
from db import Base, engine


logger = telebot.logger
logger.setLevel(logging.INFO)
bot = telebot.TeleBot(os.getenv('TOKEN'))
Base.metadata.create_all(engine)
