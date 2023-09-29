import json
import logging
import os
import sys
import telebot
import requests
import telegram

from http import HTTPStatus
from dotenv import load_dotenv
from exeptions import GetAPIError, SendMessageError
from description import description

load_dotenv()

YANDEX_WEATHER_TOKEN = os.getenv('YANDEX_WEATHER_TOKEN')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
ENDPOINT = 'https://api.weather.yandex.ru/v2/forecast/'
LIMIT = 1
PARAM = ''

headers = {
    'X-Yandex-API-Key': f'{YANDEX_WEATHER_TOKEN}',
    'Content-Type': 'application/json'
}


HELP = """
/help - покажу что умею.
/show_today_forecast - показать погоду на сегодня.
/show_tomorrow_forecast - показать погоду на завтра.
/show_forecast_for_week  - показать погоду на неделю.
/show_forecast_fact  - показать погоду сейчас.
"""


def check_tokens():
    """Проверка корректности указанных токенов."""
    if not YANDEX_WEATHER_TOKEN:
        logging.critical('Отсутствуют необходимый токен: EDUCATION_TOKEN!')
        raise SystemExit('Нет необходимых токенов.')
    if not TELEGRAM_BOT_TOKEN:
        logging.critical('Отсутствуют необходимый токен: TELEGRAM_BOT_TOKEN!')
        raise SystemExit('Нет необходимых токенов.')
    if not TELEGRAM_CHAT_ID:
        logging.critical('Отсутствуют необходимый токен: TELEGRAM_CHAT_ID!')
        raise SystemExit('Нет необходимых токенов.')
    return True


def get_api_answer(LIMIT):
    """Получение ответа от API."""
    params = {
            'lat': 59.9342802,
            'lon': 30.3350986,
            'lang': 'ru_RU',
            'limit': LIMIT
    }
    try:
        response = requests.get(ENDPOINT, headers=headers, params=params)
        if response.status_code != HTTPStatus.OK:
            raise ConnectionError(
                f'Нет ответа, код ошибки: {response.status_code}.'
            )
    except requests.RequestException('Something wrong'):
        raise GetAPIError(
            f'Нет ответа на запрос! Параметры запроса: '
            f'{ENDPOINT}, {headers}, {params}.'
        )
    data = json.loads(response.content)
    return data


def check_response(response):
    """Проверка ответа."""
    if not (isinstance(response, dict)):
        raise TypeError('Неверный формат данных.')
    if type(response) is None:
        raise TypeError('Нет данных.')
    return True


def show_response(response, PARAM):
    data = response.get(PARAM)
    forecast = description(data)
    return forecast


def send_message(bot, message):
    """Отправка сообщения в телеграмм."""
    try:
        bot.send_message(TELEGRAM_CHAT_ID, message)
        logging.debug('Сообщение отправлено.')
        sys.exit(0)
    except telegram.error.TelegramError as error:
        logging.error(f'Сообщение не отправлено! {error}.', exc_info=True)
        raise SendMessageError(f'Сообщение не отправлено! {error}')


def main(LIMIT, PARAM):
    """Основная логика работы бота."""
    check_tokens()

    while True:
        try:
            response = get_api_answer(LIMIT)
            check_response(response)
            forecast = show_response(response, PARAM)
            if forecast:
                send_message(bot, forecast)
        except SendMessageError:
            pass
        except Exception as error:
            message = f'Сбой в работе программы: {error}.'
            logging.error(f'Сбой в работе программы: {error}.', exc_info=True)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        handlers=[
            logging.FileHandler('program.log'),
            logging.StreamHandler(stream=sys.stdout)
        ],
        format='%(asctime)s, %(levelname)s, %(message)s',
        encoding='utf-8'
    )

    bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

    @bot.message_handler(commands=['start'])
    def start(message):
        bot.reply_to(message,
                     "Привет! Хочешь узнать прогноз погоды?. "
                     "Напиши /help, чтобы узнать, что я умею.")


    @bot.message_handler(commands=['help'])
    def help(message):
        bot.send_message(message.chat.id, HELP)


    @bot.message_handler(commands=['show_today_forecast'])
    def show_today_forecast(message):
        # LIMIT = 1
        PARAM = 'hour'
        main(LIMIT, PARAM)


    @bot.message_handler(commands=['show_tomorrow_forecast'])
    def show_tomorrow_forecast(message):
        LIMIT = 2
        PARAM = 'forecasts'
        main(LIMIT, PARAM)


    @bot.message_handler(commands=['show_forecast_for_week'])
    def show_forecast_for_week(message):
        LIMIT = 7
        PARAM = 'forecasts'
        main(LIMIT, PARAM)


    @bot.message_handler(commands=['show_forecast_fact'])
    def show_forecast_fact(message):
        LIMIT = 1
        PARAM = 'fact'
        main(LIMIT, PARAM)

    bot.polling()


