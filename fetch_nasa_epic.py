from pathlib import Path
import datetime
import requests

import download_image


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
