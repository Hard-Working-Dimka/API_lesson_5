import os.path
from pathlib import Path
import requests
from environs import Env
import configargparse

from image_file_tools import download_image


def fetch_spacex_images(path, launch_id):
    Path(path).mkdir(parents=True, exist_ok=True)

    spacex_url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(spacex_url)
    decoded_response = response.json()
    for image_link_number, image_link in enumerate(
            decoded_response["links"]["flickr"]["original"]):
        download_image(image_link, os.path.join(path, f'spacex{image_link_number}.jpeg'))


def main():
    env = Env()
    env.read_env()

    command_line_parser = configargparse.ArgumentParser(
        description='Загрузка картинок космоса из NASA EPIC'
    )
    command_line_parser.add_argument('-p', '--path', default='images', help='Путь загрузки фотографий')
    command_line_parser.add_argument('-id', '--launch_id', default='latest', help='ID запуска')
    args = command_line_parser.parse_args()

    fetch_spacex_images(args.path, args.launch_id)


if __name__ == '__main__':
    main()
