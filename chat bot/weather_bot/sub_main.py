import asyncio
from googletrans import Translator

async def translate(text, type):
    translator = Translator()
    if type:
        translated = await translator.translate(text, dest="en")
        print(translated.text)
    else:
        translated = await translator.translate(text, dest="ru")
    return translated.text


def run(city, type):
    return asyncio.run(translate(city, type))