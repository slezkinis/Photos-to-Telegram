import argparse
from pathlib import Path
import os.path

import requests

from supporting_file import DIRECTORY, download_file


def fetch_spacex_launch(id):
    if id == '':
        api_url='https://api.spacexdata.com/v5/launches/latest'
    else:
        api_url = f'https://api.spacexdata.com/v5/launches/{id}'
    response = requests.get(api_url)
    response.raise_for_status()
    launch = response.json()
    photo_urls = launch['links']['flickr']['original']
    for space_photo_number, space_photo_url in enumerate(photo_urls):
        if space_photo_url == '':
            break
        path = os.path.join(DIRECTORY, f'space_{space_photo_number}.jpg')
        download_file(space_photo_url, {}, path)


if __name__ == '__main__':    
    Path(DIRECTORY).mkdir(parents=True, exist_ok=True)
    parser = argparse.ArgumentParser(description='Программа скачивает фотографии с запуска ракет от компании SpaceX')
    parser.add_argument('-i', '--id', help='ID запуска', 
                        default= '')
    args = parser.parse_args()
    fetch_spacex_launch(args.id)