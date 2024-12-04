from environs import Env


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
