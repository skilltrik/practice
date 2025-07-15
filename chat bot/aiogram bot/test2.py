import os
import asyncio

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F, types
from aiogram.types.web_app_info import WebAppInfo

load_dotenv()
bot = Bot(os.getenv('bot_token'))
dp = Dispatcher()

@dp.message(F.text == '/start')
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(keyboard=[
        [
        types.KeyboardButton(text='Открыть сайт', web_app = WebAppInfo(url='https://skilltrik.github.io/practice/?v=2')),
        ]
    ])
    await message.answer('Hello my friend', reply_markup=markup)

@dp.message(content_type=['web_app_data'])
async def web_app(message: types.Message):
    await message.answer(message.web_app_data.data)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())