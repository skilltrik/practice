from aiogram import Router, types, F
from bot.keyboards.main_kb import main_keyboard

router = Router()

@router.message(F.text == '/start')
async def start(message: types.Message):
    await message.answer('Hello my friend!', reply_markup=main_keyboard())