from pathlib import Path
import requests
import configargparse
from environs import Env

from image_file_tools import download_image


def fetch_nasa_apod(nasa_api_key, quantity, path):
    Path(path).mkdir(parents=True, exist_ok=True)

    nasa_apod_url = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key': nasa_api_key,
               'count': quantity,
               }
    response = requests.get(nasa_apod_url, params=payload)
    decoded_response = response.json()
    for image_link_number, image_information in enumerate(decoded_response):  # TODO: suppoort links for several OS
        download_image(image_information['hdurl'], f'{path}/nasa_apod_{image_link_number}.jpeg')


def main():
    env = Env()
    env.read_env()

    command_line_parser = configargparse.ArgumentParser(
        description='Загрузка картинок космоса из NASA APOD'
    )
    command_line_parser.add_argument('-p', '--path', default='images', help='Путь загрузки фотографий')
    command_line_parser.add_argument('-q', '--quantity', default=1, help='Количество фотографий')
    args = command_line_parser.parse_args()

    fetch_nasa_apod(env('NASA_API_KEY'), args.quantity, args.path)


if __name__ == '__main__':
    main()
