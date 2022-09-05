"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import ephem
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(text)


def get_constellation(update, context):
    planet = update.message.text.split()[-1]
    if planet.lower() == 'mars':
        pl = ephem.Mars(datetime.datetime.now())
    if planet.lower() == 'jupiter':
        pl = ephem.Jupiter(datetime.datetime.now())
    if planet.lower() == 'uranus':
        pl = ephem.Uranus(datetime.datetime.now())
    if planet.lower() == 'neptune':
        pl = ephem.Neptune(datetime.datetime.now())
    if planet.lower() == 'mercury':
        pl = ephem.Mercury(datetime.datetime.now())
    if planet.lower() == 'venus':
        pl = ephem.Venus(datetime.datetime.now())
    if planet.lower() == 'saturn':
        pl = ephem.Saturn(datetime.datetime.now())
    update.message.reply_text(ephem.constellation(pl))

def main():
    mybot = Updater("КЛЮЧ, КОТОРЫЙ НАМ ВЫДАЛ BotFather", request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", get_constellation))


    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
