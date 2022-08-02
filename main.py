import requests
from pathlib import Path
import datetime
import urllib.parse
import os.path


DIRECTORY = 'images'
def fetch_spacex_launch(id):
    api_url = 'https://api.spacexdata.com/v3/launches'
    params = {'flight_id': id}
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    launch_list = response.json()
    launch_dict = dict(*launch_list)
    photo_urls = launch_dict['links']['flickr_images']
    for space_photo_number, space_photo_url in enumerate(photo_urls):
        path = f'{DIRECTORY}/space_{space_photo_number}.jpg'
        path_parts = path.split('/')
        directory = path_parts[0]
        Path(directory).mkdir(parents=True, exist_ok=True)
        response = requests.get(space_photo_url)
        response.raise_for_status()
        with open(path, 'wb') as file:
            file.write(response.content)


def reading_extension(file_url):
    encoded_string = urllib.parse.unquote(file_url)
    url_parts = urllib.parse.urlsplit(encoded_string)
    path = url_parts.path
    # (path_to_file, file_name)= os.path.split(path)
    (file_path, file_extension) = os.path.splitext(path)
    print(file_extension)


def get_day_photos():
    api_url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': 'xXPIxJ6ceTcZ1MRgFTbafRjfndDgfCQXifUvgYo1',
        'count': 30
             }
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    launch_list = response.json()
    for day_photo_number, day_photo_dict in enumerate(launch_list):
        if day_photo_dict['media_type'] == 'image':
            path = f'{DIRECTORY}/nasa_apod_{day_photo_number}.jpg'
            response = requests.get(day_photo_dict['url'])
            response.raise_for_status()
            with open(path, 'wb') as file:
                file.write(response.content)

def get_natural_photo_url():
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {
        'api_key': 'xXPIxJ6ceTcZ1MRgFTbafRjfndDgfCQXifUvgYo1'
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    images = response.json()
    for photo_number, image in enumerate(images):
        start_url = 'https://api.nasa.gov/EPIC/archive/natural'
        date = datetime.datetime.fromisoformat(image['date'])
        date = date.strftime('%Y/%m/%d')
        image_name = image['image']
        path = f'{DIRECTORY}/epic_photo_{photo_number}.png'
        params = {
        'api_key': 'xXPIxJ6ceTcZ1MRgFTbafRjfndDgfCQXifUvgYo1'
        }
        response = requests.get(
            f'{start_url}/{date}/png/{image_name}.png',
            params = params
        )
        with open(path, 'wb') as file:
            file.write(response.content)
        

    
if __name__ == '__main__':
    Path(DIRECTORY).mkdir(parents=True, exist_ok=True)
    get_natural_photo_url()
