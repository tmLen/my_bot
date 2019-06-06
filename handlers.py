from glob import glob
from random import choice

import utils

def greet_user(bot, update):
    greet = 'Привет,' + update.message.chat.first_name + '\n'
    update.message.reply_text(greet, reply_markup=utils.get_keyboard())

def send_picture(bot, update):
    bot.send_photo(chat_id=update.message.chat_id, photo=open(choice(glob('images/*.*')), 'rb'))

def send_text(bot, update):
    update.message.reply_text('text')

def get_contact(bot, update, user_data):
    print(update.message.contact)

def get_location(bot, update, user_data):
    print(update.message.location)

def talk_to_me(bot, update, user_data):
    update.message.reply_text(utils.get_user_emoji(user_data))