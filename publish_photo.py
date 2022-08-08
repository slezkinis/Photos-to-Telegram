import telegram
from dotenv import load_dotenv
import os
import random
import argparse

from supporting_file import DIRECTORY, collecting_files


def send_photo(photo):
    if photo == '':
        files = collecting_files(DIRECTORY)
        image = random.choice(files)
        with open(f'{DIRECTORY}/{image}', 'rb') as file:
            bot.send_document(chat_id=chat_id, document=file)
    else:
        with open(f'{DIRECTORY}/{photo}', 'rb') as file:
            bot.send_document(chat_id=chat_id, document=file)


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
