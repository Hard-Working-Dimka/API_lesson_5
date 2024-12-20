import os.path
import random

import telegram
from environs import Env
import configargparse


def main():
    env = Env()
    env.read_env()
    bot = telegram.Bot(token=env('TG_API_KEY'))
    chat_id = env('CHAT_ID')

    command_line_parser = configargparse.ArgumentParser(
        description='Запуск ТГ бота для выкладывания картинок'
    )
    command_line_parser.add_argument('path', help='Путь фотографии')
    args = command_line_parser.parse_args()

    if os.path.isfile(args.path):
        with open(args.path, 'rb') as file:
            bot.send_document(chat_id=chat_id, document=file)
    else:
        for files in os.walk(args.path):
            images = files[2]
        with open(os.path.join(args.path, random.choice(images)), 'rb') as file:
            bot.send_document(chat_id=chat_id, document=file)


if __name__ == '__main__':
    main()
