import asyncio
from googletrans import Translator
from datetime import datetime, timezone, timedelta

async def translate(text: str, to_en: bool):
    translator = Translator()

    if to_en:
        translated = await translator.translate(text, dest="en")
        print(translated.text)

    else:
        translated = await translator.translate(text, dest="ru")

    return translated.text

def run(city: str, to_en: bool):
    return asyncio.run(translate(city, to_en))

def data_processing(data: dict):
    timezone_offset = data['timezone']
    custom_timezone = timezone(timedelta(seconds=timezone_offset))
    utc_now = datetime.now(timezone.utc)
    local_time= utc_now.astimezone(custom_timezone).strftime("%Y-%m-%d %H:%M:%S")

    sunrise_utc = datetime.fromtimestamp(data['sys']['sunrise'], tz=timezone.utc)
    sunrise_local = sunrise_utc.astimezone(custom_timezone).strftime("%Y-%m-%d %H:%M:%S")

    sunset_utc = datetime.fromtimestamp(data['sys']['sunset'], tz=timezone.utc)
    sunset_local = sunset_utc.astimezone(custom_timezone).strftime("%Y-%m-%d %H:%M:%S")

    info = {'temp': data['main']['temp'],
            'temp_feel': data['main']['feels_like'],
            'humidity': data['main']['humidity'],
            'sky': run(data['weather'][0]['description'], False),
            'wind': data['wind']['speed'],
            'sunset': sunset_local,
            'time': local_time, 'sunrise': sunrise_local}

    return info