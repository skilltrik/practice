import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import FSInputFile, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot(os.getenv('bot_token'))
dp = Dispatcher()

@dp.message(F.t)
async def start_handler(message: types.Message):
    await message.answer('test')
    # await message.reply('test2')
    # photo = FSInputFile(path='photo.jpg')
    # await message.answer_photo(photo)

@dp.message(F.text.lower() == 'inline')
async def info(message: types.Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Site', url='https://github.com/skilltrik'),
            InlineKeyboardButton(text='Hello', callback_data='hello')
        ],
        [
            InlineKeyboardButton(text='Bye', callback_data='bye')
        ]
    ])

    await message.reply('Hello', reply_markup=markup)

@dp.message(F.text.lower() == 'reply')
async def reply(message: types.Message):
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='weather')],
            [KeyboardButton(text='Помощь')]
        ],
    resize_keyboard=True, one_time_keyboard=True
    )

    await message.answer('Выберите опцию: ', reply_markup=markup)

@dp.callback_query()
async def callback(call: types.CallbackQuery):
    await call.message.answer(call.data)

async def main():
    logging.info('bot started')
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())