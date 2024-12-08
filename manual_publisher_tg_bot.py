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
        bot.send_document(chat_id=chat_id, document=open(args.path, 'rb'))
    else:
        for files in os.walk(args.path):
            images = files[2]
        bot.send_document(chat_id=chat_id, document=open(os.path.join(args.path, random.choice(images)), 'rb'))


if __name__ == '__main__':
    main()
