import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler

import handlers
import settings


PROXY = {'proxy_url': settings.proxy_url, 'urllib3_proxy_kwargs': {'username': settings.username, 'password': settings.password}}
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO, filename='bot.log')


def main():

    mybot = Updater('750789173:AAGVvB-vFBIl66gsYLqnbzUqSVP1fh9bphM', request_kwargs=PROXY)
    dp = mybot.dispatcher

    dp.add_handler(CommandHandler('start', handlers.greet_user))
    # dp.add_handler(RegexHandler('^(Прислать изображение)$', handlers.send_picture))
    # dp.add_handler(RegexHandler('^(Прислать текст)$', handlers.send_text))
    # dp.add_handler(CommandHandler('pic', handlers.send_picture))
    # dp.add_handler(MessageHandler(Filters.contact, handlers.get_contact, pass_user_data=True))
    # dp.add_handler(MessageHandler(Filters.location, handlers.get_location, pass_user_data=True))
    # dp.add_handler(MessageHandler(Filters.text, handlers.talk_to_me, pass_user_data=True))

    mybot.start_polling()
    mybot.idle()
if __name__ == '__main__':
    main()
