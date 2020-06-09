import telebot
from telebot import types
import config
from messages import *

bot = telebot.TeleBot(config.TOKEN)

"""keybord"""


@bot.message_handler(commands=['start'])
def start(message):
    keyboard_main = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    admission = types.KeyboardButton(text='👨‍🎓 Поступление')
    fmpt = types.KeyboardButton(text='🤓 FMPT')
    pee = types.KeyboardButton(text='📝 Основной вступительный экзамен')  # pee - primary entrance exam
    about = types.KeyboardButton(text='🏫 О РФМШ')
    keyboard_main.add(admission, fmpt, pee, about)
    bot.send_message(message.chat.id, 'Что вы хотите узнать', reply_markup=keyboard_main)


@bot.message_handler(content_types=['text'])
def msg(message):
    def back(message):
        keyboard_main = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        admission = types.KeyboardButton(text='👨‍🎓 Поступление')
        fmpt = types.KeyboardButton(text='🤓 FMPT')
        pee = types.KeyboardButton(text='📝 Основной вступительный экзамен')  # pee - primary entrance exam
        about = types.KeyboardButton(text='🏫 О РФМШ')
        keyboard_main.add(admission, fmpt, pee, about)
        bot.send_message(message.chat.id, 'Что вы хотите узнать', reply_markup=keyboard_main)

    back_button = types.KeyboardButton(text='Назад')

    user_message = message.text
    if user_message not in user_messages:
        keyboard_main = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        admission = types.KeyboardButton(text='👨‍🎓 Поступление')
        fmpt = types.KeyboardButton(text='🤓 FMPT')
        pee = types.KeyboardButton(text='📝 Основной вступительный экзамен')  # pee - primary entrance exam
        about = types.KeyboardButton(text='🏫 О РФМШ')
        keyboard_main.add(admission, fmpt, pee, about)
        bot.send_message(message.chat.id, 'Извините, Ваш запрос не понятен. Пожалуйста, сформулируйте иначе?',
                         reply_markup=keyboard_main)

    else:
        if user_message == '👨‍🎓 Поступление':
            keyboard_admission = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            seven = types.KeyboardButton(text='Поступление в 7 класс')
            eight = types.KeyboardButton(text='Поступление в 8 класс')
            keyboard_admission.add(seven, eight, back_button)
            bot.send_message(message.chat.id, '👨‍🎓 Поступление', reply_markup=keyboard_admission)
        elif user_message == '🤓 FMPT':
            keyboard_fmpt = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            keyboard_fmpt.add(back_button)
            bot.send_message(message.chat.id, FMPT, reply_markup=keyboard_fmpt)
        elif user_message == '📝 Основной вступительный экзамен':
            keyboard_primery_entrnce_exam = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            seven = types.KeyboardButton(text='7 класс')
            eight = types.KeyboardButton(text='8 класс')
            keyboard_primery_entrnce_exam.add(seven, eight, back_button)
            bot.send_message(message.chat.id, '📝 Основной вступительный экзамен',
                             reply_markup=keyboard_primery_entrnce_exam)
        elif user_message == 'Поступление в 7 класс':
            admission_seven = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            admission_seven.add(back_button)
            bot.send_message(message.chat.id, '{}\n{}'.format(SEVEN_GRADE_1, SEVEN_GRADE_2),
                             reply_markup=admission_seven)
        elif user_message == 'Назад':
            back(message)


if __name__ == "__main__":
    print('eee')
    bot.polling(none_stop=True)
