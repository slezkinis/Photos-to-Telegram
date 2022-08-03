import requests
from pathlib import Path
import datetime
import urllib.parse
import os.path


DIRECTORY = 'images'




def reading_extension(file_url):
    encoded_string = urllib.parse.unquote(file_url)
    url_parts = urllib.parse.urlsplit(encoded_string)
    path = url_parts.path
    # (path_to_file, file_name)= os.path.split(path)
    (file_path, file_extension) = os.path.splitext(path)
    return file_extension

    
if __name__ == '__main__':
    Path(DIRECTORY).mkdir(parents=True, exist_ok=True)
