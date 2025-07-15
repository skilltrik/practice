from aiogram import Router, types, F
import json

router = Router()

@router.message(F.web_app_data)
async def handle_webapp_data(message: types.Message):
    data = json.loads(message.web_app_data.data)
    name = data.get('name')
    phone = data.get('phone')
    cart = data.get('cart', [])
    items = "\n".join([f"{i['name']} x {i['quantity']}" for i in cart])
    await message.answer(f"✅ Заказ принят!\nИмя: {name}\nТелефон: {phone}\nТовары:\n{items}")