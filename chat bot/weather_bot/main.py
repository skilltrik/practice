import telebot
import requests
import json
import sub_main
import time

bot = telebot.TeleBot('8055637928:AAEbPB5yWWqiXu0s3_VO6E-pO74SBqRkZkM')
API = 'a6bd4917bfa4dd81b0e524997a79c9c6'


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Название вашего города: ')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    start_time = time.time()
    city = sub_main.run(message.text.strip().lower(), True)
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        bot.reply_to(message, f"""
Погода сейчас:
Температура - {data['main']['temp']} градусов
Облачность - {sub_main.run(data['weather'][0]['description'], False)}
Ветер - {data['wind']['speed']} м/c
""")
    else:
        bot.reply_to(message, 'Неправильный город')
    start_time = start_time - time.time()
    print(start_time)
bot.polling(none_stop=True)
