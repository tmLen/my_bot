from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

PROXY = {'proxy_url': 'socks5://en.socksy.seriyps.ru:7777', 'urllib3_proxy_kwargs': {'username': 'tg-tmlen', 'password': 'q1n5spUC'}}
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO, filename='bot.log')


#function thet greets user and explain about what is this bot
def greet_user(bot, update):
    greet = 'Привет,' + update.message.chat.first_name + '\n'
    update.message.reply_text(greet)

def main():

    mybot = Updater('750789173:AAGVvB-vFBIl66gsYLqnbzUqSVP1fh9bphM', request_kwargs=PROXY)
    dp = mybot.dispatcher

    dp.add_handler(CommandHandler('start', greet_user))
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()
