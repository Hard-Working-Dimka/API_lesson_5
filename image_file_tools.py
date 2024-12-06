import urllib
import os
import requests


def get_file_extension(url):
    url_fragmants = urllib.parse.urlsplit(url, scheme='', allow_fragments=True)
    image_path = url_fragmants[2]
    escaped_filename = os.path.split(image_path)
    filename = urllib.parse.unquote(escaped_filename[1], encoding='utf-8', errors='replace')
    file_extension = os.path.splitext(filename)[1]
    return file_extension


def download_image(url, file_path):
    response = requests.get(url)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)
