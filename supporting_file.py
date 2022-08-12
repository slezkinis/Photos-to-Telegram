import requests
from pathlib import Path
import urllib.parse
import os.path
import telegram


DIRECTORY = 'images'




def reading_extension(file_url):
    encoded_string = urllib.parse.unquote(file_url)
    url_parts = urllib.parse.urlsplit(encoded_string)
    path = url_parts.path
    (file_path, file_extension) = os.path.splitext(path)
    return file_extension


def download_file(url, params, path):
    response = requests.get(url, params=params)
    with open(path, 'wb') as file:
        file.write(response.content)

def collecting_files(directory):
    files = os.listdir(directory)
    return files


def send_file(path, bot, tg_chat_id):
    with open(path, 'rb') as file:
        bot.send_document(chat_id=tg_chat_id, document=file)
