import os.path
from pathlib import Path
import datetime
import requests
import configargparse
from environs import Env

from image_file_tools import download_image


def fetch_nasa_epic(nasa_api_key, path, date):
    Path(path).mkdir(parents=True, exist_ok=True)

    nasa_epic_url = 'https://api.nasa.gov/EPIC/api/natural/date'
    payload = {'api_key': nasa_api_key,
               'natural/date': date}
    response = requests.get(nasa_epic_url, params=payload)
    decoded_response = response.json()

    for image_number, image_data in enumerate(decoded_response):
        image_datetime = decoded_response[image_number]['date']
        image_name = decoded_response[image_number]['image']
        formatted_image_datetime = datetime.datetime.fromisoformat(image_datetime)
        image_date = formatted_image_datetime.strftime('%Y/%m/%d')

        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{image_name}.png?' \
                    f'api_key={nasa_api_key}'
        download_image(image_url, os.path.join(path, f'nasa_epic_{image_number}.png'))


def main():
    env = Env()
    env.read_env()

    command_line_parser = configargparse.ArgumentParser(
        description='Загрузка картинок космоса из NASA EPIC'
    )
    command_line_parser.add_argument('-p', '--path', default='images', help='Путь загрузки фотографий')
    command_line_parser.add_argument('-d', '--date', default=datetime.date.today(),
                                     help='Формат даты: ГГГГ-ММ-ДД')
    args = command_line_parser.parse_args()

    fetch_nasa_epic(env('NASA_API_KEY'), args.path, args.date)


if __name__ == '__main__':
    main()
