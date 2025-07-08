import asyncio
from googletrans import Translator

async def main():
    translator = Translator()
    translated = await translator.translate("Makhachkala", dest="en")
    print("Перевод:", translated.text)

asyncio.run(main())
