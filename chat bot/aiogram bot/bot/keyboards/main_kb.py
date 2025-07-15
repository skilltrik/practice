from aiogram.types.web_app_info import WebAppInfo
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from bot.config import web_app_url

def main_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Открыть сайт', web_app=WebAppInfo(url=web_app_url))]
        ],
        resize_keyboard=True
    )