import argparse
from pathlib import Path
import os
from dotenv import load_dotenv

import requests

from main import DIRECTORY, reading_extension, download_file

def get_day_photos():
    api_url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': NASA_TOKEN,
        'count': 30
             }
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    launches = response.json()
    for day_photo_number, day_photo in enumerate(launches):
        if day_photo['media_type'] != 'video':
            extension = reading_extension(day_photo['url'])
            path = f'{DIRECTORY}/nasa_apod_{day_photo_number}{extension}'
            download_file(day_photo['url'], params, path)


if __name__ == '__main__':
    load_dotenv()
    NASA_TOKEN=os.environ['NASA_TOKEN']
    Path(DIRECTORY).mkdir(parents=True, exist_ok=True)
    parser = argparse.ArgumentParser(description='Программа скачивает популярные фотографии из космоса')
    args = parser.parse_args()
    get_day_photos()