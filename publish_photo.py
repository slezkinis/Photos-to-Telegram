import telegram
from dotenv import load_dotenv
import os
import random
import argparse

from main import DIRECTORY


load_dotenv()
BOT_TOKEN = os.environ['BOT_TOKEN']
CHAT_ID = '@Slezkin_Space'
bot = telegram.Bot(token=BOT_TOKEN)


def send_photo(photo):
    if photo == '':
        for root, dirs, files in os.walk('images'):
            image = random.choice(files)
            bot.send_document(chat_id=CHAT_ID, document=open(f'{root}/{image}', 'rb'))
    else:
        bot.send_document(chat_id=CHAT_ID, document=open(f'images/{photo}', 'rb'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Программа отправляет фотографию из папки images')
    parser.add_argument('-p', '--photo', help='Фото, которое нужно отправить', 
                        default='')
    args = parser.parse_args()
    send_photo(args.photo)
