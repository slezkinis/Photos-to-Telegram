import argparse
from pathlib import Path
from pprint import pprint
import datetime
import os

import requests
from dotenv import load_dotenv

from main import DIRECTORY, download_file


def get_epic_images():
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {
        'api_key': NASA_TOKEN
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    images = response.json()
    for photo_number, image in enumerate(images):
        url = 'https://api.nasa.gov/EPIC/archive/natural'
        date = datetime.datetime.fromisoformat(image['date'])
        date = date.strftime("%Y/%m/%d")
        image_name = image['image']
        path = f'{DIRECTORY}/epic_photo_{photo_number}.png'
        params = {
        'api_key': NASA_TOKEN
        }
        download_file(
            f'{url}/{date}/png/{image_name}.png', 
            params, path
            )


if __name__ == '__main__':
    load_dotenv()
    NASA_TOKEN=os.environ['NASA_TOKEN']
    Path(DIRECTORY).mkdir(parents=True, exist_ok=True)
    parser = argparse.ArgumentParser(description='Программа скачивает фото Земли из космоса')
    args = parser.parse_args()
    get_epic_images()    