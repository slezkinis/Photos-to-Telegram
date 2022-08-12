import telegram
from dotenv import load_dotenv
import os
import random
import time
import argparse

from supporting_file import DIRECTORY, collecting_files, send_file


def send_photos(time_delay):
    files = collecting_files(DIRECTORY)
    while True:
        try:
            for image in files:
                send_file(os.path.join(DIRECTORY, image), bot, tg_chat_id)
                time.sleep(time_delay)
            random.shuffle(files)
        except telegram.error.NetworkError:
            time.sleep(2)


if __name__ == '__main__':
    load_dotenv()
    tg_token = os.environ['TG_TOKEN']
    tg_chat_id = os.environ['TG_CHAT_ID']
    bot = telegram.Bot(token=tg_token)
    parser = argparse.ArgumentParser(
        description='Программа отправляет фотографии из папки images'
        )
    parser.add_argument('-d', '--delay', help='Время ожидания',
                        default=3600, type=int)
    args = parser.parse_args()
    send_photos(args.delay)
