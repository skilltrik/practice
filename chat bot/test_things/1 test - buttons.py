import telebot
from telebot import types
import datetime
import webbrowser

bot = telebot.TeleBot('8055637928:AAEbPB5yWWqiXu0s3_VO6E-pO74SBqRkZkM')

#кнопки на главном экране и приветственное смс
@bot.message_handler(commands=['start'])
def start(message):
    markap = types.ReplyKeyboardMarkup()
    markap.add(types.KeyboardButton("Скинь аватарку"))
    a = datetime.datetime(2025, 7, 7, 20, 31, 00)
    delta = datetime.datetime.now() - a
    bot.send_message(message.chat.id, f'Привет, {message.from_user.username}, прошло {datetime.timedelta(seconds=int(delta.total_seconds()))} с момента начала работы над кодом', reply_markup=markap)
    bot.register_next_step_handler(message, on_click)

#срабатывает один раз
def on_click(message):
    if message.text == "Скинь аватарку":
        photo = open('ri.webp', 'rb')
        bot.send_photo(message.chat.id, photo)


#получение всей информации из message
@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, message)

#ответы на конкретные смс
@bot.message_handler()
def reply(message):
    if message.text.lower() == 'привет':
        a = datetime.datetime(2025, 7, 7, 20, 31, 00)
        delta = datetime.datetime.now() - a
        bot.send_message(message.chat.id,f'Привет, {message.from_user.username}, прошло {datetime.timedelta(seconds=int(delta.total_seconds()))} с момента начала работы над кодом')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')
    elif message.text.lower() == 'github':
        bot.send_message(message.chat.id, 'https://github.com/skilltrik')
    elif message.text.lower() == 'open github':
        webbrowser.open('https://github.com/skilltrik')

#реагирование на фото и кнопки под сообщением
@bot.message_handler(content_types=['photo'])
def photo_buttons(message):
    markap = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Перейти на мой гитхаб", url='https://github.com/skilltrik')
    markap.row(btn1)
    btn2 = types.InlineKeyboardButton("Удалить фото", callback_data='delete')
    btn3 = types.InlineKeyboardButton("Изменить текст", callback_data='edit')
    markap.row(btn2, btn3)
    bot.reply_to(message, 'Это фото', reply_markup=markap)

#выполнение работы кнопок
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id-1)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)

bot.polling(none_stop=True)