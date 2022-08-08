from logging import exception
import telegram
from dotenv import load_dotenv
import os
import random
import time
import argparse

from main import DIRECTORY




def send_photos(time_delay):
    for root, dirs, files in os.walk(DIRECTORY):
        while True:
            try:
                for image in files:
                    bot.send_document(chat_id=chat_id, document=open(f'{root}/{image}', 'rb'))
                    time.sleep(time_delay)
                random.shuffle(files)
            except telegram.error.NetworkError:
                time.sleep(2)



if __name__ == '__main__':
    load_dotenv()
    tg_token = os.environ['TG_TOKEN']
    chat_id = '@Slezkin_Space'
    bot = telegram.Bot(token=tg_token)
    parser = argparse.ArgumentParser(description='Программа отправляет фотографии из папки images')
    parser.add_argument('-d', '--delay', help='Время ожидания', 
                        default=3600, type=int)
    args = parser.parse_args()
    send_photos(args.delay)
