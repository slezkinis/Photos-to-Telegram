import argparse
from pathlib import Path
import os.path

import requests

from supporting_file import DIRECTORY, download_file


def fetch_spacex_launch(launch_id):
    api_url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(api_url)
    response.raise_for_status()
    launch = response.json()
    photo_urls = launch['links']['flickr']['original']
    for photo_number, photo_url in enumerate(photo_urls):
        path = os.path.join(DIRECTORY, f'space_{photo_number}.jpg')
        download_file(photo_url, {}, path)


if __name__ == '__main__':    
    Path(DIRECTORY).mkdir(parents=True, exist_ok=True)
    parser = argparse.ArgumentParser(description='Программа скачивает фотографии с запуска ракет от компании SpaceX')
    parser.add_argument('-i', '--id', help='ID запуска', 
                        default= 'latest')
    args = parser.parse_args()
    fetch_spacex_launch(args.id)