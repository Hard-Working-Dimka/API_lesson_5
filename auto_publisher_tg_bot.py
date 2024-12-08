import os.path
import time
import random

import telegram
from environs import Env
import configargparse
from pytimeparse import parse


def main():
    env = Env()
    env.read_env()
    bot = telegram.Bot(token=env('TG_API_KEY'))
    chat_id = env('CHAT_ID')

    command_line_parser = configargparse.ArgumentParser(
        description='Запуск ТГ бота для выкладывания картинок'
    )
    command_line_parser.add_argument('-p', '--path', default='images', env_var='PATH',
                                     help='Путь загрузки фотографий')
    command_line_parser.add_argument('-per', '--publication_period', default='4h',
                                     env_var='PUBLICATION_PERIOD', help='Период отправки фотографий')
    args = command_line_parser.parse_args()

    for files in os.walk(args.path):
        images = files[2]
    while True:
        for image in images:
            bot.send_document(chat_id=chat_id, document=open(os.path.join(args.path, image), 'rb'))
            time.sleep(parse(args.publication_period))
        random.shuffle(images)


if __name__ == '__main__':
    main()
