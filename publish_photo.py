import telegram
from dotenv import load_dotenv
import os
import random
import argparse

from supporting_file import DIRECTORY


def send_photo(photo):
    if photo == '':
        for root, dirs, files in os.walk('images'):
            image = random.choice(files)
            bot.send_document(chat_id=chat_id, document=open(f'{root}/{image}', 'rb'))
    else:
        bot.send_document(chat_id=chat_id, document=open(f'{DIRECTORY}/{photo}', 'rb'))


if __name__ == '__main__':
    load_dotenv()
    tg_token = os.environ['TG_TOKEN']
    chat_id = os.environ['CHAT_ID']
    bot = telegram.Bot(token=tg_token)
    parser = argparse.ArgumentParser(description='Программа отправляет фотографию из папки images')
    parser.add_argument('-p', '--photo', help='Фото, которое нужно отправить', 
                        default='')
    args = parser.parse_args()
    send_photo(args.photo)
