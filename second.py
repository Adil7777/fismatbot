import telebot
from telebot import types
import config
from messages import *
from db import *
import asyncio
from datetime import datetime

bot = telebot.TeleBot(config.TOKEN)
init_db()


def main(id, text):
    keyboard_main = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    admission = types.KeyboardButton(text='👨‍🎓 Поступление')
    fmpt = types.KeyboardButton(text='🤓 FMPT')
    pee = types.KeyboardButton(text='📝 Основной вступительный экзамен')  # pee - primary entrance exam
    about = types.KeyboardButton(text='🏫 Ученикам')
    fund = types.KeyboardButton(text='💳 Fizmat Endowment Fund')
    keyboard_main.add(admission, fmpt, pee, about, fund)
    bot.send_message(id, text, reply_markup=keyboard_main)


def fund(id, text):
    keybord_fund = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    what_is_it = types.KeyboardButton(text='🤷‍♂️Что такое? 🤷‍♀')
    better = types.KeyboardButton(text='В чем же преимущество')
    who_can_be = types.KeyboardButton(text='👨 Кто может стать участником 👩')
    support = types.KeyboardButton(text='💹 Сделать вклад')
    keybord_fund.add(what_is_it, better, who_can_be, support, back_button)
    bot.send_message(id, text, reply_markup=keybord_fund)


def exam(id, text):
    keyboard_primery_entrance_exam = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    seven = types.KeyboardButton(text='7 класс')
    eight = types.KeyboardButton(text='8 класс')
    keyboard_primery_entrance_exam.add(seven, eight, back_button)
    bot.send_message(id, text, reply_markup=keyboard_primery_entrance_exam)


def admission_(id, text):
    keyboard_admission = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    seven = types.KeyboardButton(text='Поступление в 7 класс')
    eight = types.KeyboardButton(text='Поступление в 8 класс')
    keyboard_admission.add(seven, eight, back_button)
    bot.send_message(id, text, reply_markup=keyboard_admission)


def school(id, text):
    keyboard_school = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    exams = types.KeyboardButton(text='АКР')
    timetable = types.KeyboardButton(text='Расписание')
    keyboard_school.add(exams, timetable, back_button)
    bot.send_message(id, text, reply_markup=keyboard_school)


def akr(id, text):
    keyboard_akr = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    first = types.KeyboardButton(text='7-10 классы')
    second = types.KeyboardButton(text='11 классы')
    keyboard_akr.add(first, second, back_button)
    bot.send_message(id, text, reply_markup=keyboard_akr)


"""keybord"""

back_button = types.KeyboardButton(text='Назад')


@bot.message_handler(commands=['start'])
def start(message):
    add_user(message.chat.id, True)
    main(message.chat.id, 'Что вы хотите узнать')


@bot.message_handler(content_types=['text'])
def msg(message):
    user_message = message.text
    # print(message.from_user.id)
    id = message.chat.id
    if user_message not in user_messages:
        main(id, 'Извините, Ваш запрос не понятен. Пожалуйста, сформулируйте иначе?')

    else:
        if user_message == '👨‍🎓 Поступление':
            admission_(id, '👨‍🎓 Поступление')

        elif user_message == 'АКР':
            akr(id, 'АКР')

        elif user_message == 'Расписание':
            pass

        elif user_message == '🏫 Ученикам':
            school(id, '🏫 Ученикам')

        elif user_message == '🤓 FMPT':
            main(id, FMPT)

        elif user_message == '📝 Основной вступительный экзамен':
            exam(id, '📝 Основной вступительный экзамен')

        elif user_message == '💳 Fizmat Endowment Fund':
            fund(id, '💳 Fizmat Endowment Fund')

        elif user_message == 'Поступление в 7 класс':
            admission_(id, '{}\n{}'.format(SEVEN_GRADE_1, SEVEN_GRADE_2))

        elif user_message == 'Поступление в 8 класс':
            admission_(id, EIGHT_GRADE)

        elif user_message == '7 класс':
            exam(id, PEE_7)

        elif user_message == '8 класс':
            exam(id, PEE_8)

        elif user_message == '🤷‍♂️Что такое? 🤷‍♀':
            fund(id, WHAT_IS_IT)

        elif user_message == 'В чем же преимущество':
            fund(id, BETTER)

        elif user_message == '👨 Кто может стать участником 👩':
            fund(id, WHO_CAN_BE)

        elif user_message == '💹 Сделать вклад':
            fund(id, DONATE)

        elif user_message == 'Назад':
            main(id, 'Что вы хотите узнать')


async def schedule(wait_for):
    while 1:
        await asyncio.sleep(wait_for)

        now = datetime.utcnow()
        await main(755715325, str(now))


if __name__ == "__main__":
    print('program starting')
    bot.polling(none_stop=True)
