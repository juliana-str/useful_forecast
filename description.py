import sys
from datetime import datetime

DAY_PART = {'night': 'НОЧЬЮ', 'morning': 'УТРОМ', 'day': 'ДНЕМ',
            'evening': 'ВЕЧЕРОМ', 'fact': 'СЕЙЧАС'}
COLD = 'Прохладно, не забудь взять шапку и перчатки!'
WARM = 'Теплая погодка, можно погулять!'
NORM = 'Еще не холодно, не сиди дома!'

CONDITIONS = {'clear': 'ясно', 'partly-cloudy': 'малооблачно',
              'cloudy': 'облачно с прояснениями', 'overcast': 'пасмурно',
              'drizzle': 'морось', 'light-rain': 'небольшой дождь',
              'rain': 'дождь', 'moderate-rain': 'умеренно сильный',
              'heavy-rain': 'сильный дождь',
              'continuous-heavy-rain': 'длительный сильный дождь',
              'showers': 'ливень', 'wet-snow': 'дождь со снегом',
              'light-snow': 'небольшой снег', 'snow': 'снег',
              'snow-showers': 'снегопад', 'hail': 'град',
              'thunderstorm': 'гроза',
              'thunderstorm-with-rain': 'дождь с грозой',
              'thunderstorm-with-hail': 'гроза с градом'}

WIND_DIR = {'nw': 'северо-западное', 'n': 'северное', 'ne': 'северо-восточное',
            'e': 'восточное', 'se': 'юго-восточное', 's': 'южное',
            'sw': 'юго-западное', 'w': 'западное', 'с': 'штиль'}

day = datetime.today().strftime('%d. %B %Y')


def parse_today_data(data):
    temp = data.get('temp')
    feels_like = data.get('feels_like')
    condition = data.get('condition')
    wind_speed = data.get('wind_speed')
    wind_dir = data.get('wind_dir')
    humidity = data.get('humidity')
    temp_water = data.get('temp_water')
    is_thunder = data.get('is_thunder')
    hint = ''

    if temp_water > 19:
        hint += 'Водичка теплая можно купаться!'
    if int(temp) >= 15:
        hint += WARM
    elif 5 < int(temp) < 15:
        hint += NORM
    else:
        hint += COLD
    if is_thunder:
        hint += 'Осторожно, ожидается гроза!'

    return (f'Сегодня, {day} '
            f'температура воздуха - {temp}°C (ощущается как - {feels_like}), '
            f'{CONDITIONS[condition]}, '
            f'скорость порывов ветра - {wind_speed}, '
            f'направление ветра - {WIND_DIR[wind_dir]}, '
            f'влажность воздуха {humidity}%, '
            f'{hint} ')


def parse_data_for_days(data):
    forecast_for_days = []
    for day in data:
        forecast_for_days.append(day.get('date'))
        for part, weather in day['parts'].items():
            if part in DAY_PART.keys():
                daypart = DAY_PART.get(part)
                temp_avg = weather.get('temp_avg')
                wind_speed = weather.get('wind_speed')
                wind_dir = weather.get('wind_dir')
                humidity = weather.get('humidity')
                feels_like = weather.get('feels_like')
                condition = weather.get('condition')
                forecast_for_part = (
                    f'{daypart} температура воздуха {temp_avg}°C '
                    f'(ощущается как {feels_like}), '
                    f'{CONDITIONS[condition]}, '
                    f'скорость порывов ветра - {wind_speed}, '
                    f'направление ветра - {WIND_DIR[wind_dir]}, '
                    f'влажность воздуха {humidity}%. '
                    f'                                        ')
                forecast_for_days.append(forecast_for_part)
            if len(data) == 2 and len(forecast_for_days) == 2:
                forecast_for_days = forecast_for_days[1]
                break
    return ' '.join(forecast_for_days)


def parse_data_for_week(data):
    forecast_for_days = []
    for day in data:
        forecast_for_days.append(day.get('date'))
        for part, weather in day['parts'].items():
            if part in DAY_PART.keys():
                daypart = DAY_PART.get(part)
                temp_avg = weather.get('temp_avg')
                feels_like = weather.get('feels_like')
                forecast_for_part = (
                    f'{daypart} температура воздуха {temp_avg}°C ({feels_like})')

                forecast_for_days.append(forecast_for_part)
    return ' '.join(forecast_for_days)


def description(data):
    if not isinstance(data, list):
        return parse_today_data(data)
    else:
        if len(data) == 1:
            return parse_data_for_days(data)
        elif len(data) == 2:
            return parse_data_for_days(data)
        else:
            return parse_data_for_week(data)
