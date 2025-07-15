import os
from dotenv import load_dotenv

load_dotenv()
bot_token = os.getenv('bot_token')
web_app_url = os.getenv('web_app_url')