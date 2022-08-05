import requests
from pathlib import Path
import datetime
import urllib.parse
import os.path
from dotenv import load_dotenv


DIRECTORY = 'images'




def reading_extension(file_url):
    encoded_string = urllib.parse.unquote(file_url)
    url_parts = urllib.parse.urlsplit(encoded_string)
    path = url_parts.path
    # (path_to_file, file_name)= os.path.split(path)
    (file_path, file_extension) = os.path.splitext(path)
    return file_extension


def download_file(url, params, path):
    response = requests.get(url, params=params)
    with open(path, 'wb') as file:
        file.write(response.content)

    
if __name__ == '__main__':
    load_dotenv()
    Path(DIRECTORY).mkdir(parents=True, exist_ok=True)
