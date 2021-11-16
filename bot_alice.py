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
    return random.randint(len(list))


def say_good_morning(my_id):
    a = ['волшебная', 'восхитительная', 'замечательная', 'любимая', 'кайфовая', 'дружная']
    b = ['приятнейшего', 'позитивного', 'танцевального', 'свежего', 'прогулочного']
    c = []

    message = f'Доброе утро, моя {a[get_pril(a)]} семья! Желаю вам {b[get_pril(b)]} дня! Люблю вас всех!'

    return bot.send_message(my_id, message)


def say_test(my_id):


    message = f'test'

    return bot.send_message(my_id, message)

def say_good_evening(my_id):
    a = ['волшебная', 'восхитительная', 'замечательная', 'любимая', 'кайфовая', 'дружная']
    b = ['почищу зубки', 'помассирую Шанечку', 'слопаю 45 пельмешков', 'повозюкаю маркерами на обоях', 'покричу на пылесос']
    c = []

    message = f'Спокойной ночи, моя {a[get_pril(a)]} семья! Пойду {b[get_pril(b)]} и буду ложиться спать! Люблю вас всех!'

    return bot.send_message(my_id, message)


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
