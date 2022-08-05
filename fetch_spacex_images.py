import argparse
from pathlib import Path

import requests

from main import DIRECTORY, download_file


def fetch_spacex_launch(id):
    if id == '':
        api_url='https://api.spacexdata.com/v5/launches/latest'
        params = {}
    else:
        api_url = 'https://api.spacexdata.com/v3/launches'
        params = {'flight_id': id}
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    launch = response.json()
    if id == '':
        photo_urls = launch['links']['flickr']['original']
    else:
        launch = dict(*launch)
        photo_urls = launch['links']['flickr_images']
    for space_photo_number, space_photo_url in enumerate(photo_urls):
        if space_photo_url == '':
            break
        path = f'{DIRECTORY}/space_{space_photo_number}.jpg'
        download_file(space_photo_url, params, path)


if __name__ == '__main__':    
    Path(DIRECTORY).mkdir(parents=True, exist_ok=True)
    parser = argparse.ArgumentParser(description='Программа скачивает фотографии с запуска ракет от компании SpaceX')
    parser.add_argument('-i', '--id', help='ID запуска', 
                        default= '')
    args = parser.parse_args()
    fetch_spacex_launch(args.id)