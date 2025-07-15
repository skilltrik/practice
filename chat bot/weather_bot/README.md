# Weather_bot
## Описание
### Бот принимает название города от пользователя, переводит его на английский язык (через Google Translate), делает запрос к OpenWeatherMap API и возвращает форматированную информацию о погоде: температуру, влажность, облачность, ветер, время рассвета и заката, а также локальное время.
___________________

## Стек технологий

    Python 3.10+

    python-telegram-bot / pyTelegramBotAPI (telebot)

    requests

    googletrans

    python-dotenv

    OpenWeatherMap API

___________________

## Проблемы
### Разделение обязанностей, логики и т.п.
### Проблема заключается в том, что подобное разделение на функции, а тем более файлы для чистой архитектуры - излишне Функция бота - показывать время, погоду и чуть-чуть дополнительной информации, которую предоставляет сервис с помощью API. Этой информации просто недостаточно для того, чтобы добавлять функции в бота позже и расширять его.
### Если бы информации было как от yandex weather, я бы с удовольствием расширял полезный функционал, но так как надобности в этом нет, то и разделения чистого тоже.
___________________

## Остальное
### Если кто-нибудь знает более качественный сервис по получению данных, пожалуйста напишите, прошу учитывать, что я гражданин РФ, и поэтому, из-за неимения международной банковской карты, должен обходиться полностью бесплатными сервисами, которые не требуют обязательного ввода данных карты. 
___________________

## Для тех, кто хочет использовать
### 1. Создайте .env файл и добавьте туда свои ключи:
    bot_token=ВАШ_ТОКЕН_БОТА
    weather_api=ВАШ_КЛЮЧ_ОТ_OPENWEATHERMAP
### 2. Установите зависимости:
    pip install -r requirements.txt
### 3. И запуск через main.py
___________________

## Примечания
### Бот поддерживает любой язык ввода — город автоматически переводится на английский. Возможны ошибки из-за неофициальной библиотеки (простите)
### При ошибке подключения или неправильном городе выведется сообщение об ошибке.
### Все токены и ключи находятся в .env — не загружайте их в публичный репозиторий.


___________________


# Weather_bot
## Description
### The bot receives a city name from the user, translates it into English (using Google Translate), sends a request to the OpenWeatherMap API, and returns formatted weather information: temperature, humidity, cloudiness, wind speed, sunrise and sunset times, as well as local time.
___________________

## Tech Stack

    Python 3.10+

    python-telegram-bot / pyTelegramBotAPI (telebot)

    requests

    googletrans

    python-dotenv

    OpenWeatherMap API
___________________

## Issues
### Separation of responsibilities and logic

### The main problem is that dividing such a simple bot into multiple functions or even files for the sake of clean architecture is excessive.
### The bot's only purpose is to display time, weather, and a bit of additional info provided by the API.
### This information is not sufficient to justify further modularization or the implementation of scalable architecture.
### If the service provided as much data as, for example, Yandex Weather, I would be happy to expand the bot's functionality.
### However, since there's no such need, a fully clean architectural approach feels unnecessary here.
___________________

## Other

### If anyone knows of a better weather data provider, please let me know.
### Please keep in mind that I am a citizen of the Russian Federation, and due to the lack of an international bank card, I can only use completely free services that do not require entering card details.
___________________

## How to Use

### 1. Create a .env file and add your tokens:

    bot_token=YOUR_BOT_TOKEN
    weather_api=YOUR_OPENWEATHERMAP_API_KEY

### 2. Install the dependencies:

    pip install -r requirements.txt

### 3. Run main.py
___________________

## Notes

###    The bot supports input in any language — the city name is automatically translated into English. Translation errors may occur due to the use of an unofficial library (sorry!).
###    If there’s a connection error or the city is invalid, the bot will return an error message.
###    All tokens and keys are stored in the .env file — do not upload it to public repositories.