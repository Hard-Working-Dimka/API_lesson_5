from pathlib import Path
import requests

import download_image


def fetch_spacex_last_launch(url, path):
    Path(path).mkdir(parents=True, exist_ok=True)
    response = requests.get(url)
    decoded_response = response.json()
    for image_link_number, image_link in enumerate(
            decoded_response["links"]["flickr"]["original"]):  # TODO: suppoort links for several OS
        download_image(image_link, f'{path}/spacex{image_link_number}.jpeg')
