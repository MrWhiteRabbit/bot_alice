import telebot
import datetime
from auth_data import auth_data


bot = telebot.TeleBot(auth_data)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/help':
        bot.send_message(message.chat.id, '/age - покажу возраст в днях.')
    elif message.text == '/age':
        startdate = '2020-06-05'.split('-')
        enddate = str(datetime.date.today()).split('-')  # '2021-11-14'.split('-')
        sd = datetime.date(int(startdate[0]), int(startdate[1]), int(startdate[2]))
        ed = datetime.date(int(enddate[0]), int(enddate[1]), int(enddate[2]))
        fd = str(ed - sd).split()[0]
        bot.send_message(message.chat.id, f'Сегодня мне {fd} дней!')


bot.polling(none_stop=True, interval=0)