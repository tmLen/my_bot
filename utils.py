from emoji import emojize
from random import choice
from telegram import ReplyKeyboardMarkup, KeyboardButton

import settings

def get_user_emoji(user_data):
    if 'smile' not in user_data:
        user_data['smile'] = emojize(choice(settings.USER_EMOJI), use_aliases=True)
    return user_data['smile']

def get_keyboard():
    contact_button = KeyboardButton('Контактные данные', request_contact=True)
    location_button = KeyboardButton('Местоположение', request_location=True)
    my_keyboard = ReplyKeyboardMarkup([
        ['Прислать изображение', 'Прислать текст'], 
        [contact_button, location_button]
        ], resize_keyboard=True)
    return my_keyboard