import urllib
import os


def get_file_extension(url):
    url_fragmants = urllib.parse.urlsplit(url, scheme='', allow_fragments=True)
    image_path = url_fragmants[2]
    escaped_filename = os.path.split(image_path)
    filename = urllib.parse.unquote(escaped_filename[1], encoding='utf-8', errors='replace')
    file_extension = os.path.splitext(filename)[1]
