import telegram
from dotenv import load_dotenv
import os


load_dotenv()
BOT_TOKEN = os.environ['BOT_TOKEN']
bot = telegram.Bot(token=BOT_TOKEN)
bot.send_message(chat_id='@Slezkin_Space', text='Всем привет! Это тестовое сообщение!')
