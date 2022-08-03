import telegram
from dotenv import load_dotenv
import os
import random
import time
import argparse

from main import DIRECTORY


load_dotenv()
BOT_TOKEN = os.environ['BOT_TOKEN']
CHAT_ID = '@Slezkin_Space'
bot = telegram.Bot(token=BOT_TOKEN)

def send_photos(time_delay):
    for root, dirs, files in os.walk('images'):
        while True:
            for image in files:
                bot.send_document(chat_id=CHAT_ID, document=open(f'{root}/{image}', 'rb'))
                time.sleep(time_delay)
            random.shuffle(files)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Программа отправляет фотографии из папки images')
    parser.add_argument('-d', '--delay', help='Время ожидания', 
                        default=os.environ['DELAY'], type=int)
    args = parser.parse_args()
    send_photos(args.delay)
