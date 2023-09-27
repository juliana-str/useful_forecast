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
              'thunderstorm-with-hail': 'гроза с градом'
}

WIND_DIR = {'nw': 'северо-западное', 'n': 'северное', 'ne': 'северо-восточное',
            'e': 'восточное', 'se': 'юго-восточное', 's': 'южное',
            'sw': 'юго-западное', 'w': 'западное', 'с': 'штиль'}


def description(data):
    forecast = []
    if not isinstance(data, list):
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

        pogoda = (f''
                f'Температура воздуха - {temp}, °C (ощущается как - {feels_like}), '
                f'{CONDITIONS[condition]}, ' \
                f'скорость порывов ветра - {wind_speed}, ' \
                f'направление ветра - {WIND_DIR[wind_dir]}, ' \
                f'влажность воздуха {humidity}%, ' \
                f'{hint}.')
        forecast.append(pogoda)

    else:
         for day in data:
             temp = day.get('temp')
             feels_like = day.get('feels_like')
             condition = day.get('condition')
             wind_speed = day.get('wind_speed')
             wind_dir = day.get('wind_dir')
             humidity = day.get('humidity')
             temp_water = day.get('temp_water')
             is_thunder = day.get('is_thunder')
             hint = ''

             if int(temp_water) > 19:
                 hint += 'Водичка теплая можно купаться!'
             if int(temp) >= 15:
                 hint += WARM
             elif 5 < int(temp) < 15:
                 hint += NORM
             else:
                 hint += COLD
             if is_thunder:
                 hint += 'Осторожно, ожидается гроза!'

             pogoda = (f''
                       f'Температура воздуха - {temp}, °C (ощущается как - {feels_like}), '
                       f'{CONDITIONS[condition]}, ' \
                       f'скорость порывов ветра - {wind_speed}, ' \
                       f'направление ветра - {WIND_DIR[wind_dir]}, ' \
                       f'влажность воздуха {humidity}%, ' \
                       f'{hint}.')
             forecast.append(pogoda)

    return forecast
