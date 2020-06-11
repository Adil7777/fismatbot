from aiogram import types, Bot, Dispatcher, executor
import config
from messages import *
from db import *
import asyncio
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
bot = Bot(config.TOKEN)
dp = Dispatcher(bot)
init_db()


def main():
    keyboard_main = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    admission = types.KeyboardButton(text='👨‍🎓 Поступление')
    fmpt = types.KeyboardButton(text='🤓 FMPT')
    pee = types.KeyboardButton(text='📝 Вступительный экзамен')  # pee - primary entrance exam
    about = types.KeyboardButton(text='🏫 Ученикам')
    fund = types.KeyboardButton(text='💳 Fizmat Endowment Fund')
    keyboard_main.add(admission, fmpt, pee, about, fund)
    return keyboard_main
    # bot.send_message(id, text, reply_markup=keyboard_main)


def fund():
    keybord_fund = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    what_is_it = types.KeyboardButton(text='🤷‍♂️Что такое? 🤷‍♀')
    better = types.KeyboardButton(text='В чем же преимущество')
    who_can_be = types.KeyboardButton(text='👨 Кто может стать участником 👩')
    support = types.KeyboardButton(text='💹 Сделать вклад')
    keybord_fund.add(what_is_it, better, who_can_be, support, back_button)
    return keybord_fund


def exam():
    keyboard_primery_entrance_exam = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    seven = types.KeyboardButton(text='7 класс')
    eight = types.KeyboardButton(text='8 класс')
    keyboard_primery_entrance_exam.add(seven, eight, back_button)
    return keyboard_primery_entrance_exam


def admission_():
    keyboard_admission = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    seven = types.KeyboardButton(text='Поступление в 7 класс')
    eight = types.KeyboardButton(text='Поступление в 8 класс')
    keyboard_admission.add(seven, eight, back_button)
    return keyboard_admission


def school():
    keyboard_school = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    exams = types.KeyboardButton(text='АКР')
    timetable = types.KeyboardButton(text='Расписание')
    keyboard_school.add(exams, timetable, back_button)
    return keyboard_school


def akr():
    keyboard_akr = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    first = types.KeyboardButton(text='7-10 классы')
    second = types.KeyboardButton(text='11 классы')
    keyboard_akr.add(first, second, back_button)
    return keyboard_akr


"""keybord"""

back_button = types.KeyboardButton(text='Назад')


@dp.message_handler(commands=['start'])
async def start(message):
    if not subscriber_exist(message.chat.id):
        add_user(message.chat.id, True)
    keyboard_main = main()
    await bot.send_message(message.chat.id, 'Что вы хотите узнать', reply_markup=keyboard_main)


@dp.message_handler(content_types=['text'])
async def msg(message):
    user_message = message.text
    id = message.chat.id
    if user_message not in user_messages:
        keyboard_main = main()
        await bot.send_message(id, 'Извините, Ваш запрос не понятен. Пожалуйста, сформулируйте иначе?',
                               reply_markup=keyboard_main)

    else:
        if user_message == '👨‍🎓 Поступление':
            keyboard_main = admission_()
            await bot.send_message(id, '👨‍🎓 Поступление', reply_markup=keyboard_main)

        elif user_message == 'АКР':
            keyboard_main = akr()
            await bot.send_message(id, 'АКР', reply_markup=keyboard_main)

        elif user_message == 'Расписание':
            pass

        elif user_message == '🏫 Ученикам':
            keyboard_main = school()
            await bot.send_message(id, '🏫 Ученикам', reply_markup=keyboard_main)

        elif user_message == '🤓 FMPT':
            keyboard_main = main()
            await bot.send_message(id, FMPT, reply_markup=keyboard_main)

        elif user_message == '📝 Вступительный экзамен':
            keyboard_main = exam()
            await bot.send_message(id, '📝 Вступительный экзамен', reply_markup=keyboard_main)

        elif user_message == '💳 Fizmat Endowment Fund':
            keyboard_main = fund()
            await bot.send_message(id, '💳 Fizmat Endowment Fund', reply_markup=keyboard_main)

        elif user_message == 'Поступление в 7 класс':
            keyboard_main = admission_()
            await bot.send_message(id, '{}\n{}'.format(SEVEN_GRADE_1, SEVEN_GRADE_2), reply_markup=keyboard_main)

        elif user_message == 'Поступление в 8 класс':
            keyboard_main = admission_()
            await bot.send_message(id, EIGHT_GRADE, reply_markup=keyboard_main)

        elif user_message == '7 класс':
            keyboard_main = exam()
            await bot.send_message(id, PEE_7, reply_markup=keyboard_main)

        elif user_message == '8 класс':
            keyboard_main = exam()
            await bot.send_message(id, PEE_8, reply_markup=keyboard_main)

        elif user_message == '🤷‍♂️Что такое? 🤷‍♀':
            keyboard_main = fund()
            await bot.send_message(id, WHAT_IS_IT, reply_markup=keyboard_main)

        elif user_message == 'В чем же преимущество':
            keyboard_main = fund()
            await bot.send_message(id, BETTER, reply_markup=keyboard_main)

        elif user_message == '👨 Кто может стать участником 👩':
            keyboard_main = fund()
            await bot.send_message(id, WHO_CAN_BE, reply_markup=keyboard_main)

        elif user_message == '💹 Сделать вклад':
            keyboard_main = fund()
            await bot.send_message(id, DONATE, reply_markup=keyboard_main)

        elif user_message == 'Назад':
            keyboard_main = main()
            await bot.send_message(id, 'Что вы хотите узнать', reply_markup=keyboard_main)


async def schedule(wait_for):
    while 1:
        await asyncio.sleep(wait_for)

        now = datetime.utcnow()
        await bot.send_message('755715325', str(now), disable_notification=True)


if __name__ == "__main__":
    print('program starting')
    # dp.loop.create_task(schedule(10))
    executor.start_polling(dp, skip_updates=True)
