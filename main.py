import pprint  # TODO: DELETE!
from pathlib import Path
import urllib
import os
import datetime

import requests
from environs import Env


def download_image(url, path):
    response = requests.get(url)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch(url, path):
    Path(path).mkdir(parents=True, exist_ok=True)
    response = requests.get(url)
    decoded_response = response.json()
    for image_link_number, image_link in enumerate(
            decoded_response["links"]["flickr"]["original"]):  # TODO: suppoort links for several OS
        download_image(image_link, f'{path}/spacex{image_link_number}.jpeg')


def get_file_extension(url):
    url_fragmants = urllib.parse.urlsplit(url, scheme='', allow_fragments=True)
    image_path = url_fragmants[2]
    escaped_filename = os.path.split(image_path)
    filename = urllib.parse.unquote(escaped_filename[1], encoding='utf-8', errors='replace')
    file_extension = os.path.splitext(filename)[1]


def get_nasa_apod_images(url, nasa_api_key, quantity, path):
    Path(path).mkdir(parents=True, exist_ok=True)

    payload = {'api_key': nasa_api_key,
               'count': quantity,
               }
    response = requests.get(url, params=payload)
    decoded_response = response.json()
    for image_link_number, image_information in enumerate(decoded_response):  # TODO: suppoort links for several OS
        download_image(image_information['hdurl'], f'{path}/nasa_apod_{image_link_number}.jpeg')


def get_nasa_epic_images(url, nasa_api_key, path, date):
    Path(path).mkdir(parents=True, exist_ok=True)

    payload = {'api_key': nasa_api_key,
               'natural/date': date}
    response = requests.get(url, params=payload)
    decoded_response = response.json()

    for image_number, image_data in enumerate(decoded_response):
        image_datetime = decoded_response[image_number]['date']
        image_name = decoded_response[image_number]['image']
        formatted_image_datetime = datetime.datetime.fromisoformat(image_datetime)
        image_date = formatted_image_datetime.strftime('%Y/%m/%d')

        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{image_name}.png?' \
                    f'api_key={nasa_api_key}'
        download_image(image_url, f'{path}/nasa_epic_{image_number}.png')


def main():
    env = Env()
    env.read_env()

    spacex_url = 'https://api.spacexdata.com/v5/launches/5eb87d42ffd86e000604b384'
    nasa_apod_url = 'https://api.nasa.gov/planetary/apod'
    nasa_epic_url = 'https://api.nasa.gov/EPIC/api/natural/date'

    #   get_nasa_apod_images(nasa_apod_url,env('NASA_API_KEY'), 3, 'images')
    get_nasa_epic_images(nasa_epic_url, env('NASA_API_KEY'), 'test/', '2019-05-30')


if __name__ == '__main__':
    main()
