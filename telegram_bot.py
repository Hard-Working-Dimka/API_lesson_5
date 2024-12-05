import telegram
from environs import Env


def main():
    env = Env()
    env.read_env()
    bot = telegram.Bot(token=env('TG_API_KEY'))
    print(bot.get_me())

    bot.send_message(chat_id='@kfjfisnwhfiwjd', text="I'm sorry Dave I'm afraid I can't do that.")


if __name__ == '__main__':
    main()
