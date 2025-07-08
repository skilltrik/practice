import telebot
import requests
import json
import util
import os
from dotenv import load_dotenv

load_dotenv()

bot_token = os.getenv('bot_token')
API = os.getenv('weather_api')
bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Название вашего города: ')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = util.run(message.text.strip().lower(), True)

    try:
        res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')

        if res.status_code == 200:
            info = util.data_processing(json.loads(res.text))
            msg = f"""<b>🌤 Погода в городе</b>
------------------------------------------
🕒 <b>Время:</b> {info['time']}

🌅 <b>Рассвет:</b> {info['sunrise']}

🌇 <b>Закат:</b> {info['sunset']}
------------------------------------------

------------------------------------------
🌡 <b>Температура:</b> {info['temp']}°C

🥶 <b>Ощущается как:</b> {info['temp_feel']}°C
------------------------------------------

------------------------------------------
☁️ <b>Облачность:</b> {info['sky']}

💨 <b>Ветер:</b> {info['wind']} м/с

💧 <b>Влажность:</b> {info['humidity']}%
------------------------------------------
"""
            bot.send_message(message.chat.id, msg, parse_mode='html')

        else:
            bot.reply_to(message, 'Неправильный город')

    except requests.exceptions.RequestException as e:
        bot.reply_to(message, f"❌ Ошибка подключения")
        return

bot.polling(none_stop=True)
