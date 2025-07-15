import asyncio
from aiogram import Bot, Dispatcher
from bot.config import bot_token
from bot.handlers import start, webapp

async def main():
    bot = Bot(bot_token)
    dp = Dispatcher()
    dp.include_router(start.router)
    dp.include_router(webapp.router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())