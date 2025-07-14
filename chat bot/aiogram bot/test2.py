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
    markup = types.InlineKeyboardMarkup(inline_keyboard=[
        [
        types.InlineKeyboardButton(text='Открыть сайт', web_app = WebAppInfo(url='https://github.com/skilltrik')),
        ]
    ])
    await message.answer('Hello my friend', reply_markup=markup)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())