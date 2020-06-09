from aiogram import Bot, Dispatcher, executor, types
import config
import logging
import messages

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

"""Sending information to user about admission to grade 7"""


@dp.message_handler(commands=['7_grade'])
async def seven_grade(message: types.Message):
    await message.answer(messages.SEVEN_GRADE_1)
    await message.answer(messages.SEVEN_GRADE_2)


"""Sending information to user about admission to grade 7"""


@dp.message_handler(commands=['8_grade'])
async def eight_grade(message: types.Message):
    await message.answer(messages.EIGHT_GRADE)


@dp.message_handler(commands=['fmpt'])
async def eight_grade(message: types.Message):
    await message.answer(messages.FMPT)


@dp.message_handler(commands=['primary_entrance_exam_7'])
async def eight_grade(message: types.Message):
    await message.answer(messages.PEE_7)


@dp.message_handler(commands=['primary_entrance_exam_8'])
async def eight_grade(message: types.Message):
    await message.answer(messages.PEE_8)


"""If user don't know what write to bot, we send him this message"""


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(messages.BASIC)


"""If everything is ok, we start our program"""
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
