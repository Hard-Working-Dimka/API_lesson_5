import telegram
from environs import Env


def main():
    env = Env()
    env.read_env()
    bot = telegram.Bot(token=env('TG_API_KEY'))

    chat_id = '@kfjfisnwhfiwjd'

    #  bot.send_message(chat_id=chat_id, text="I'm sorry Dave I'm afraid I can't do that.")
    bot.send_document(chat_id=chat_id,
                      document=open(
                          'D:\\Projects\\PYTHON\\Lessons\\Web Services API\\API_lesson_5\\images\\nasa_apod_0.jpeg',
                          'rb'))  # TODO: использовать os.path.join


if __name__ == '__main__':
    main()
