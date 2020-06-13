"""import tools"""
from aiogram import Bot, Dispatcher, executor
import asyncio
import logging

from messages import *
from db import DataBase
from keyboard import Keyboard
from news import News
from exams_parser import Exam, Themes
import config

"""Initialization"""

exam = Exam()
logging.basicConfig(level=logging.INFO)
bot = Bot(config.TOKEN)
dp = Dispatcher(bot)
Database = DataBase()
Database.init_db()
keyboard = Keyboard()
news = News('news.txt')
themes = Themes()

"""keybord"""


@dp.message_handler(commands=['start'])
async def start(message):
    Database.add_user(message.chat.id, True)
    keyboard_main = keyboard.main()
    await bot.send_message(message.chat.id, 'Что вы хотите узнать', reply_markup=keyboard_main)


@dp.message_handler(content_types=['text'])
async def msg(message):
    user_message = message.text
    id = message.chat.id
    keyboard_main = keyboard.main()
    send_text = None
    if user_message not in user_messages:
        await bot.send_message(id, 'Извините, Ваш запрос не понятен. Пожалуйста, сформулируйте иначе?',
                               reply_markup=keyboard_main)

    else:
        if user_message == '👨‍🎓 Поступление':
            keyboard_main = keyboard.admission_()
            send_text = '👨‍🎓 Поступление'

        elif user_message == 'АКР':
            keyboard_main = keyboard.akr()
            send_text = 'АКР'

        elif user_message == 'Расписание':
            pass

        elif user_message == '🏫 Ученикам':
            keyboard_main = keyboard.school()
            send_text = '🏫 Ученикам'

        elif user_message == '🤓 FMPT':
            keyboard_main = keyboard.main()
            send_text = FMPT

        elif user_message == '📝 Вступительный экзамен':
            keyboard_main = keyboard.exam()
            send_text = '📝 Вступительный экзамен'

        elif user_message == '💳 Fizmat Endowment Fund':
            keyboard_main = keyboard.fund()
            send_text = '💳 Fizmat Endowment Fund'

        elif user_message == 'Поступление в 7 класс':
            keyboard_main = keyboard.admission_()
            send_text = '{}\n{}'.format(SEVEN_GRADE_1, SEVEN_GRADE_2)

        elif user_message == 'Поступление в 8 класс':
            keyboard_main = keyboard.admission_()
            send_text = EIGHT_GRADE

        elif user_message == '7 класс':
            keyboard_main = keyboard.exam()
            send_text = PEE_7

        elif user_message == '8 класс':
            keyboard_main = keyboard.exam()
            send_text = PEE_8

        elif user_message == '🤷‍♂️Что такое? 🤷‍♀':
            keyboard_main = keyboard.fund()
            send_text = WHAT_IS_IT

        elif user_message == 'В чем же преимущество':
            keyboard_main = keyboard.fund()
            send_text = BETTER

        elif user_message == '👨 Кто может стать участником 👩':
            keyboard_main = keyboard.fund()
            send_text = WHO_CAN_BE

        elif user_message == '💹 Сделать вклад':
            keyboard_main = keyboard.fund()
            send_text = DONATE

        elif user_message == 'Назад':
            keyboard_main = keyboard.main()
            send_text = 'Что вы хотите узнать'

        elif user_message == '7-10 классы предметы':
            keyboard_main = keyboard.akr()
            send_text = EXAMS

        elif user_message == '11 классы предметы':
            keyboard_main = keyboard.akr()
            send_text = exam.parse_11()

        elif user_message == 'Темы':
            keyboard_main = keyboard.akr()
            first, second, third = themes.parse()
            send_text = '1 четверть {}\n\n2 четверть {}\n\n3 четверть{}'.format(first, second, third)

        await bot.send_message(id, send_text, reply_markup=keyboard_main)


async def schedule(wait_for):
    while 1:
        await asyncio.sleep(wait_for)

        user_ids = Database.get_users()
        if not news.new_news():
            href, text = news.get_href()
            href, text = str(href), str(text)
            for user_id in user_ids:
                await bot.send_message(user_id, text + '\n' + href, disable_notification=True)


if __name__ == "__main__":
    print('program starting')
    dp.loop.create_task(schedule(10))
    executor.start_polling(dp, skip_updates=True)
