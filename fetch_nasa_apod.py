from pathlib import Path
import requests

import download_image

def get_nasa_apod_images(url, nasa_api_key, quantity, path):
    Path(path).mkdir(parents=True, exist_ok=True)

    payload = {'api_key': nasa_api_key,
               'count': quantity,
               }
    response = requests.get(url, params=payload)
    decoded_response = response.json()
    for image_link_number, image_information in enumerate(decoded_response):  # TODO: suppoort links for several OS
        download_image(image_information['hdurl'], f'{path}/nasa_apod_{image_link_number}.jpeg')
