from aiogram import types


class Keyboard:
    def __init__(self):
        self.back_button = types.KeyboardButton(text='Назад')

    def main(self):
        keyboard_main = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        admission = types.KeyboardButton(text='👨‍🎓 Поступление')
        fmpt = types.KeyboardButton(text='🤓 FMPT')
        pee = types.KeyboardButton(text='📝 Вступительный экзамен')  # pee - primary entrance exam
        about = types.KeyboardButton(text='🏫 Ученикам')
        fund = types.KeyboardButton(text='💳 Fizmat Endowment Fund')
        keyboard_main.add(admission, fmpt, pee, about, fund)
        return keyboard_main

    def fund(self):
        keybord_fund = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        what_is_it = types.KeyboardButton(text='🤷‍♂️Что такое? 🤷‍♀')
        better = types.KeyboardButton(text='В чем же преимущество')
        who_can_be = types.KeyboardButton(text='👨 Кто может стать участником 👩')
        support = types.KeyboardButton(text='💹 Сделать вклад')
        keybord_fund.add(what_is_it, better, who_can_be, support, self.back_button)
        return keybord_fund

    def exam(self):
        keyboard_primery_entrance_exam = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        seven = types.KeyboardButton(text='7 класс')
        eight = types.KeyboardButton(text='8 класс')
        keyboard_primery_entrance_exam.add(seven, eight, self.back_button)
        return keyboard_primery_entrance_exam

    def admission_(self):
        keyboard_admission = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        seven = types.KeyboardButton(text='Поступление в 7 класс')
        eight = types.KeyboardButton(text='Поступление в 8 класс')
        keyboard_admission.add(seven, eight, self.back_button)
        return keyboard_admission

    def school(self):
        keyboard_school = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        exams = types.KeyboardButton(text='АКР')
        timetable = types.KeyboardButton(text='Расписание')
        keyboard_school.add(exams, timetable, self.back_button)
        return keyboard_school

    def akr(self):
        keyboard_akr = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        first = types.KeyboardButton(text='7-10 классы предметы')
        second = types.KeyboardButton(text='11 классы предметы')
        themes = types.KeyboardButton(text='Темы')
        keyboard_akr.add(first, second, themes, self.back_button)
        return keyboard_akr
