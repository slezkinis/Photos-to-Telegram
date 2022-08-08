import requests
from pathlib import Path
import urllib.parse
import os.path


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
    for root, dirs, files in os.walk(directory):
        return files
