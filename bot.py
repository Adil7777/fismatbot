from aiogram import Bot, Dispatcher, executor, types
import config
import logging

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(message.text)


@dp.message_handler(commands=['7'])
async def seven_grade(message: types.Message):
    await message.answer("7 класс")


@dp.message_handler(commands=['8'])
async def eight_grade(message: types.Message):
    await message.answer("8 класс")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
