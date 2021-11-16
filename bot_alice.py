#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import telebot
import datetime
import random
import schedule
from threading import Thread
from time import sleep
from auth_data import auth_data
from auth_data import chat_id

bot = telebot.TeleBot(auth_data)


def schedule_checker():

    schedule.run_pending()
    sleep(1)


def poll():

    bot.polling(none_stop=True, interval=0)


def get_pril(list):
    return random.randint(0, len(list)-1)


def say_good_morning(my_id):
    a = ['волшебная',
         'восхитительная',
         'замечательная',
         'любимая',
         'кайфовая',
         'дружная',
         'весёлая',
         'большая',
         'милая',
         'могучая',
         'музыкальная',
         'творческая',
         'позитивная',
         'креативная'
         ]

    b = ['приятнейшего',
         'позитивного',
         'танцевального',
         'свежего',
         'прогулочного',
         'весёлого',
         'интересного',
         'доброго',
         'вкусного',
         'эмоционального',
         'продуктивного',
         'раслабленного',
         'головокружительного',
         'тёплого',
         'цветастого',
         'музыкального'
         ]

    message = f'Доброе утро, моя {a[get_pril(a)]} семья! Желаю вам {b[get_pril(b)]} дня! Люблю вас всех!'

    return bot.send_message(my_id, message)


def say_test(my_id):

    message = f'test'

    return bot.send_message(my_id, message)


def say_good_evening(my_id):
    a = ['волшебная',
         'восхитительная',
         'замечательная',
         'любимая',
         'кайфовая',
         'дружная',
         'весёлая',
         'большая',
         'милая',
         'могучая',
         'музыкальная',
         'творческая',
         'позитивная',
         'креативная'
         ]
    b = ['почищу зубки',
         'помассирую Шанечку',
         'слопаю 45 пельмешков',
         'повозюкаю маркерами на обоях',
         'покричу на пылесос',
         'покружусь на стуле',
         'поору на Шанечку',
         'покружусь в танце',
         'почитаю книжечку',
         'посмотрю еще один мультик',
         'скушаю фруктовую пюрешку',
         'слопаю печеньку',
         'раскидаю вещички из шкафчика',
         'покатаюсь на машинке (бип-бииип!)',
         'потыкаю папину клавиатуру',
         'постучу по крышке маминого ноутбука',
         'поцелую папу и маму',
         'отправлю вам воздушный поцелуйчик',
         'напою своих пушистых собачек',
         'подюдюкаю',
         'подядякаю',
         'найду свою бутылочку и соску',
         'подмету ковер',
         'раскидаю игрушки',
         'посижу на Шанином домике',
         'покатаюсь на Шани',
         'попью водички'
         ]

    message = f'Спокойной ночи, моя {a[get_pril(a)]} семья! Пойду {b[get_pril(b)]} и буду ложиться спать! Люблю вас всех!'
    print(message)
    return bot.send_message(my_id, message)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/help':
        bot.send_message(message.chat.id, '/age - покажу возраст в днях.')
    elif message.text == '/age':
        startdate = '2020-06-04'.split('-')
        enddate = str(datetime.date.today()).split('-')  # '2021-11-14'.split('-')
        sd = datetime.date(int(startdate[0]), int(startdate[1]), int(startdate[2]))
        ed = datetime.date(int(enddate[0]), int(enddate[1]), int(enddate[2]))
        fd = str(ed - sd).split()[0]
        bot.send_message(message.chat.id, f'Сегодня мне {fd} дней!')


if __name__ == '__main__':
    try:

        schedule.every().day.at("09:00").do(say_good_morning, chat_id)
        schedule.every().day.at("21:00").do(say_good_evening, chat_id)
    # schedule.every().day.at("17:58").do(say_test, chat_id)

        Thread(target=poll).start()

        while True:
            schedule_checker()

    except Exception as e:
        print(e)
