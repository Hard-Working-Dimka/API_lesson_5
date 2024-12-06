import telegram
from environs import Env
import configargparse


def main():
    env = Env()
    env.read_env()
    bot = telegram.Bot(token=env('TG_API_KEY'))

    command_line_parser = configargparse.ArgumentParser(
        description='Запуск ТГ бота для выкладывания картинок'
    )
    command_line_parser.add_argument('path', help='Путь фотографии')
    args = command_line_parser.parse_args()

    bot.send_document(chat_id=env('CHAT_ID'), document=open(args.path, 'rb'))


if __name__ == '__main__':
    main()
