forecasts = [
        {'date': '2023-09-29',
         'parts':
             {'night': {'temp_min': 11, 'temp_avg': 12, 'temp_max': 13,
                        'wind_speed': 1.9, 'wind_dir': 'se', 'humidity': 91,
                        'soil_temp': 11, 'soil_moisture': 0.31, 'prec_mm': 0,
                        'prec_prob': 0, 'prec_period': 360, 'cloudness': 0.5,
                        'prec_type': 0, 'prec_strength': 0, 'icon': 'bkn_n',
                        'condition': 'cloudy', 'uv_index': 0, 'feels_like': 11,
                        'daytime': 'n', 'polar': False, 'fresh_snow_mm': 0},
             'night_short': {'_source': '0,1,2,3,4,5', 'temp': 11,
                              'wind_speed': 1.9, 'wind_gust': 5.2,
                              'wind_dir': 'se', 'pressure_mm': 765,
                              'pressure_pa': 1019, 'humidity': 91,
                              'soil_temp': 11, 'soil_moisture': 0.31,
                              'prec_mm': 0, 'prec_prob': 0, 'prec_period': 360,
                              'cloudness': 0.5, 'prec_type': 0,
                              'prec_strength': 0, 'icon': 'bkn_n',
                              'condition': 'cloudy', 'uv_index': 0,
                              'feels_like': 11, 'daytime': 'n', 'polar': False,
                              'fresh_snow_mm': 0},
              'day': {'_source': '12,13,14,15,16,17', 'temp_min': 17,
                      'temp_avg': 20, 'temp_max': 21, 'wind_speed': 3.3,
                      'wind_gust': 7.2, 'wind_dir': 's', 'pressure_mm': 761,
                      'pressure_pa': 1014, 'humidity': 69, 'soil_temp': 17,
                      'soil_moisture': 0.31, 'prec_mm': 0, 'prec_prob': 0,
                      'prec_period': 360, 'cloudness': 0.75, 'prec_type': 0,
                      'prec_strength': 0, 'icon': 'bkn_d',
                      'condition': 'cloudy', 'uv_index': 1, 'feels_like': 19,
                      'daytime': 'd', 'polar': False, 'fresh_snow_mm': 0},
              'morning': {'_source': '6,7,8,9,10,11', 'temp_min': 12,
                          'temp_avg': 14, 'temp_max': 16, 'wind_speed': 2.8,
                          'wind_gust': 6.9, 'wind_dir': 's',
                          'pressure_mm': 763, 'pressure_pa': 1016,
                          'humidity': 89, 'soil_temp': 13,
                          'soil_moisture': 0.31, 'prec_mm': 0, 'prec_prob': 0,
                          'prec_period': 360, 'cloudness': 0.75,
                          'prec_type': 0, 'prec_strength': 0, 'icon': 'bkn_d',
                          'condition': 'cloudy', 'uv_index': 1,
                          'feels_like': 13, 'daytime': 'd', 'polar': False,
                          'fresh_snow_mm': 0},
              'day_short': {
                      '_source': '6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21',
                      'temp': 21, 'temp_min': 12, 'wind_speed': 3.3,
                      'wind_gust': 7.2, 'wind_dir': 's', 'pressure_mm': 761,
                      'pressure_pa': 1014, 'humidity': 78, 'soil_temp': 16,
                      'soil_moisture': 0.31, 'prec_mm': 0, 'prec_prob': 0,
                      'prec_period': 960, 'cloudness': 0.75, 'prec_type': 0,
                      'prec_strength': 0, 'icon': 'bkn_d',
                      'condition': 'cloudy', 'uv_index': 1, 'feels_like': 16,
                      'daytime': 'd', 'polar': False, 'fresh_snow_mm': 0},
              'evening': {'_source': '18,19,20,21', 'temp_min': 18,
                          'temp_avg': 19, 'temp_max': 20, 'wind_speed': 2.6,
                          'wind_gust': 5.9, 'wind_dir': 's',
                          'pressure_mm': 759, 'pressure_pa': 1011,
                          'humidity': 75, 'soil_temp': 17,
                          'soil_moisture': 0.31, 'prec_mm': 0, 'prec_prob': 0,
                          'prec_period': 240, 'cloudness': 1, 'prec_type': 0,
                          'prec_strength': 0, 'icon': 'ovc',
                          'condition': 'overcast', 'uv_index': 0,
                          'feels_like': 19, 'daytime': 'n', 'polar': False,
                          'fresh_snow_mm': 0}},
         'hours': [{'hour': '0', 'hour_ts': 1695934800, 'temp': 12,
                    'feels_like': 11, 'icon': 'ovc', 'condition': 'overcast',
                    'cloudness': 1, 'prec_type': 0, 'prec_strength': 0,
                    'is_thunder': False, 'wind_dir': 'se', 'wind_speed': 1.2,
                    'wind_gust': 2.7, 'pressure_mm': 765, 'pressure_pa': 1019,
                    'humidity': 92, 'uv_index': 0, 'soil_temp': 11,
                    'soil_moisture': 0.31, 'prec_mm': 0, 'prec_period': 60,
                    'prec_prob': 0},
                   {'hour': '1', 'hour_ts': 1695938400, 'temp': 12,
                    'feels_like': 11, 'icon': 'bkn_n', 'condition': 'cloudy',
                    'cloudness': 0.5, 'prec_type': 0, 'prec_strength': 0,
                    'is_thunder': False, 'wind_dir': 'se', 'wind_speed': 1.5,
                    'wind_gust': 3.4, 'pressure_mm': 765, 'pressure_pa': 1019,
                    'humidity': 91, 'uv_index': 0, 'soil_temp': 11,
                    'soil_moisture': 0.31, 'prec_mm': 0, 'prec_period': 60,
                    'prec_prob': 0},
                   {'hour': '2', 'hour_ts': 1695942000, 'temp': 11,
                    'feels_like': 10, 'icon': 'bkn_n', 'condition': 'cloudy',
                    'cloudness': 0.5, 'prec_type': 0, 'prec_strength': 0,
                    'is_thunder': False, 'wind_dir': 'se', 'wind_speed': 1.7,
                    'wind_gust': 4.1, 'pressure_mm': 765, 'pressure_pa': 1019,
                    'humidity': 90, 'uv_index': 0, 'soil_temp': 11,
                    'soil_moisture': 0.31, 'prec_mm': 0, 'prec_period': 60,
                    'prec_prob': 0},
                   {'hour': '3', 'hour_ts': 1695945600, 'temp': 11,
                    'feels_like': 11, 'icon': 'bkn_n', 'condition': 'cloudy',
                    'cloudness': 0.5, 'prec_type': 0, 'prec_strength': 0,
                    'is_thunder': False, 'wind_dir': 'se', 'wind_speed': 1.5,
                    'wind_gust': 5.1, 'pressure_mm': 765, 'pressure_pa': 1019,
                    'humidity': 88, 'uv_index': 0, 'soil_temp': 10,
                    'soil_moisture': 0.31, 'prec_mm': 0, 'prec_period': 60,
                    'prec_prob': 0},
                   {'hour': '4', 'hour_ts': 1695949200, 'temp': 13,
                    'feels_like': 11, 'icon': 'bkn_n', 'condition': 'cloudy',
                    'cloudness': 0.5, 'prec_type': 0, 'prec_strength': 0,
                    'is_thunder': False, 'wind_dir': 'se', 'wind_speed': 1.6,
                    'wind_gust': 4.4, 'pressure_mm': 764, 'pressure_pa': 1018,
                    'humidity': 91, 'uv_index': 0, 'soil_temp': 11,
                    'soil_moisture': 0.31, 'prec_mm': 0, 'prec_period': 60,
                    'prec_prob': 0},
                   {'hour': '5', 'hour_ts': 1695952800, 'temp': 13,
                    'feels_like': 11, 'icon': 'bkn_n', 'condition': 'cloudy',
                    'cloudness': 0.5, 'prec_type': 0, 'prec_strength': 0,
                    'is_thunder': False, 'wind_dir': 'se', 'wind_speed': 1.8,
                    'wind_gust': 4.5, 'pressure_mm': 764, 'pressure_pa': 1018,
                    'humidity': 91, 'uv_index': 0, 'soil_temp': 11,
                    'soil_moisture': 0.31, 'prec_mm': 0, 'prec_period': 60,
                    'prec_prob': 0},
                   {'hour': '6', 'hour_ts': 1695956400, 'temp': 12,
                    'feels_like': 11, 'icon': 'bkn_n', 'condition': 'cloudy',
                    'cloudness': 0.5, 'prec_type': 0, 'prec_strength': 0,
                    'is_thunder': False, 'wind_dir': 'se', 'wind_speed': 1.8,
                    'wind_gust': 4.1, 'pressure_mm': 763, 'pressure_pa': 1017,
                    'humidity': 90, 'uv_index': 0, 'soil_temp': 12,
                    'soil_moisture': 0.31, 'prec_mm': 0, 'prec_period': 60,
                    'prec_prob': 0},
                   {'hour': '7', 'hour_ts': 1695960000, 'temp': 14,
                    'feels_like': 11, 'icon': 'bkn_d', 'condition': 'cloudy',
                    'cloudness': 0.5, 'prec_type': 0, 'prec_strength': 0,
                    'is_thunder': False, 'wind_dir': 'se', 'wind_speed': 1.8,
                    'wind_gust': 4.6, 'pressure_mm': 763, 'pressure_pa': 1017,
                    'humidity': 91, 'uv_index': 0, 'soil_temp': 12,
                    'soil_moisture': 0.31, 'prec_mm': 0, 'prec_period': 60,
                    'prec_prob': 0},
                   {'hour': '8', 'hour_ts': 1695963600, 'temp': 14,
                    'feels_like': 11, 'icon': 'bkn_d', 'condition': 'cloudy',
                    'cloudness': 0.5, 'prec_type': 0, 'prec_strength': 0,
                    'is_thunder': False, 'wind_dir': 'se', 'wind_speed': 2,
                    'wind_gust': 5.8, 'pressure_mm': 763, 'pressure_pa': 1017,
                    'humidity': 92, 'uv_index': 0, 'soil_temp': 13,
                    'soil_moisture': 0.31, 'prec_mm': 0, 'prec_period': 60,
                    'prec_prob': 0},
                   {'hour': '9', 'hour_ts': 1695967200, 'temp': 14,
                    'feels_like': 13, 'icon': 'bkn_d', 'condition': 'cloudy',
                    'cloudness': 0.5, 'prec_type': 0, 'prec_strength': 0,
                    'is_thunder': False, 'wind_dir': 's', 'wind_speed': 2,
                    'wind_gust': 6.5, 'pressure_mm': 762, 'pressure_pa': 1015,
                    'humidity': 91, 'uv_index': 0, 'soil_temp': 13,
                    'soil_moisture': 0.31, 'prec_mm': 0, 'prec_period': 60,
                    'prec_prob': 0},
                   {'hour': '10', 'hour_ts': 1695970800, 'temp': 15,
                    'feels_like': 14, 'icon': 'ovc', 'condition': 'overcast',
                    'cloudness': 1, 'prec_type': 0, 'prec_strength': 0,
                    'is_thunder': False, 'wind_dir': 's', 'wind_speed': 2.7,
                    'wind_gust': 6.9, 'pressure_mm': 762, 'pressure_pa': 1015,
                    'humidity': 88, 'uv_index': 1, 'soil_temp': 14,
                    'soil_moisture': 0.31, 'prec_mm': 0, 'prec_period': 60,
                    'prec_prob': 0},
                   {'hour': '11', 'hour_ts': 1695974400, 'temp': 16,
                    'feels_like': 16, 'icon': 'ovc', 'condition': 'overcast',
                    'cloudness': 1, 'prec_type': 0, 'prec_strength': 0,
                    'is_thunder': False, 'wind_dir': 's', 'wind_speed': 2.7,
                    'wind_gust': 6.5, 'pressure_mm': 762, 'pressure_pa': 1015,
                    'humidity': 83, 'uv_index': 1, 'soil_temp': 15,
                    'soil_moisture': 0.31, 'prec_mm': 0, 'prec_period': 60,
                    'prec_prob': 0},
                   {'hour': '12', 'hour_ts': 1695978000, 'temp': 17,
                    'feels_like': 18, 'icon': 'ovc', 'condition': 'overcast',
                    'cloudness': 1, 'prec_type': 0, 'prec_strength': 0,
                    'is_thunder': False, 'wind_dir': 's', 'wind_speed': 2.5,
                    'wind_gust': 6.8, 'pressure_mm': 761, 'pressure_pa': 1014,
                    'humidity': 77, 'uv_index': 1, 'soil_temp': 16,
                    'soil_moisture': 0.31, 'prec_mm': 0, 'prec_period': 60,
                    'prec_prob': 0},
                   {'hour': '13', 'hour_ts': 1695981600, 'temp': 20,
                    'feels_like': 19, 'icon': 'bkn_d', 'condition': 'cloudy',
                    'cloudness': 0.75, 'prec_type': 0, 'prec_strength': 0,
                    'is_thunder': False, 'wind_dir': 's', 'wind_speed': 2.7,
                    'wind_gust': 6.6, 'pressure_mm': 761, 'pressure_pa': 1014,
                    'humidity': 70, 'uv_index': 1, 'soil_temp': 16,
                    'soil_moisture': 0.31, 'prec_mm': 0, 'prec_period': 60,
                    'prec_prob': 0},
                   {'hour': '14', 'hour_ts': 1695985200, 'temp': 20,
                    'feels_like': 20, 'icon': 'bkn_d', 'condition': 'cloudy',
                    'cloudness': 0.5, 'prec_type': 0, 'prec_strength': 0,
                    'is_thunder': False, 'wind_dir': 's', 'wind_speed': 3.2,
                    'wind_gust': 7, 'pressure_mm': 761, 'pressure_pa': 1014,
                    'humidity': 69, 'uv_index': 1, 'soil_temp': 17,
                    'soil_moisture': 0.31, 'prec_mm': 0, 'prec_period': 60,
                    'prec_prob': 0},
                   {'hour': '15', 'hour_ts': 1695988800, 'temp': 20,
                    'feels_like': 21, 'icon': 'bkn_d', 'condition': 'cloudy',
                    'cloudness': 0.5, 'prec_type': 0, 'prec_strength': 0,
                    'is_thunder': False, 'wind_dir': 's', 'wind_speed': 3.2,
                    'wind_gust': 7.1, 'pressure_mm': 760, 'pressure_pa': 1013,
                    'humidity': 64, 'uv_index': 1, 'soil_temp': 18,
                    'soil_moisture': 0.31, 'prec_mm': 0, 'prec_period': 60,
                    'prec_prob': 0},
                   {'hour': '16', 'hour_ts': 1695992400, 'temp': 21,
                    'feels_like': 21, 'icon': 'bkn_d', 'condition': 'cloudy',
                    'cloudness': 0.5, 'prec_type': 0, 'prec_strength': 0,
                    'is_thunder': False, 'wind_dir': 's', 'wind_speed': 3,
                    'wind_gust': 6.6, 'pressure_mm': 760, 'pressure_pa': 1013,
                    'humidity': 65, 'uv_index': 1, 'soil_temp': 18,
                    'soil_moisture': 0.31, 'prec_mm': 0, 'prec_period': 60,
                    'prec_prob': 0},
                   {'hour': '17', 'hour_ts': 1695996000, 'temp': 21,
                    'feels_like': 21, 'icon': 'ovc', 'condition': 'overcast',
                    'cloudness': 1, 'prec_type': 0, 'prec_strength': 0,
                    'is_thunder': False, 'wind_dir': 's', 'wind_speed': 2.9,
                    'wind_gust': 6.3, 'pressure_mm': 760, 'pressure_pa': 1013,
                    'humidity': 67, 'uv_index': 0, 'soil_temp': 18,
                    'soil_moisture': 0.31, 'prec_mm': 0, 'prec_period': 60,
                    'prec_prob': 0},
                   {'hour': '18', 'hour_ts': 1695999600, 'temp': 20,
                    'feels_like': 20, 'icon': 'ovc', 'condition': 'overcast',
                    'cloudness': 1, 'prec_type': 0, 'prec_strength': 0,
                    'is_thunder': False, 'wind_dir': 's', 'wind_speed': 2.5,
                    'wind_gust': 5.9, 'pressure_mm': 759, 'pressure_pa': 1011,
                    'humidity': 70, 'uv_index': 0, 'soil_temp': 17,
                    'soil_moisture': 0.31, 'prec_mm': 0, 'prec_period': 60,
                    'prec_prob': 0},
                   {'hour': '19', 'hour_ts': 1696003200, 'temp': 19,
                    'feels_like': 18, 'icon': 'ovc', 'condition': 'overcast',
                    'cloudness': 1, 'prec_type': 0, 'prec_strength': 0,
                    'is_thunder': False, 'wind_dir': 's', 'wind_speed': 2.5,
                    'wind_gust': 5.8, 'pressure_mm': 759, 'pressure_pa': 1011,
                    'humidity': 74, 'uv_index': 0, 'soil_temp': 17,
                    'soil_moisture': 0.31, 'prec_mm': 0, 'prec_period': 60,
                    'prec_prob': 0},
                   {'hour': '20', 'hour_ts': 1696006800, 'temp': 18,
                    'feels_like': 17, 'icon': 'ovc', 'condition': 'overcast',
                    'cloudness': 1, 'prec_type': 0, 'prec_strength': 0,
                    'is_thunder': False, 'wind_dir': 's', 'wind_speed': 2.5,
                    'wind_gust': 5.5, 'pressure_mm': 759, 'pressure_pa': 1011,
                    'humidity': 77, 'uv_index': 0, 'soil_temp': 17,
                    'soil_moisture': 0.31, 'prec_mm': 0, 'prec_period': 60,
                    'prec_prob': 0},
                   {'hour': '21', 'hour_ts': 1696010400, 'temp': 18,
                    'feels_like': 17, 'icon': 'ovc', 'condition': 'overcast',
                    'cloudness': 1, 'prec_type': 0, 'prec_strength': 0,
                    'is_thunder': False, 'wind_dir': 's', 'wind_speed': 2.2,
                    'wind_gust': 5.4, 'pressure_mm': 759, 'pressure_pa': 1011,
                    'humidity': 80, 'uv_index': 0, 'soil_temp': 16,
                    'soil_moisture': 0.31, 'prec_mm': 0, 'prec_period': 60,
                    'prec_prob': 0},
                   {'hour': '22', 'hour_ts': 1696014000, 'temp': 17,
                    'feels_like': 17, 'icon': 'ovc', 'condition': 'overcast',
                    'cloudness': 1, 'prec_type': 0, 'prec_strength': 0,
                    'is_thunder': False, 'wind_dir': 'sw', 'wind_speed': 2.5,
                    'wind_gust': 5, 'pressure_mm': 758, 'pressure_pa': 1010,
                    'humidity': 80, 'uv_index': 0, 'soil_temp': 16,
                    'soil_moisture': 0.31, 'prec_mm': 0, 'prec_period': 60,
                    'prec_prob': 0},
                   {'hour': '23', 'hour_ts': 1696017600, 'temp': 17,
                    'feels_like': 16, 'icon': 'ovc', 'condition': 'overcast',
                    'cloudness': 1, 'prec_type': 0, 'prec_strength': 0,
                    'is_thunder': False, 'wind_dir': 'sw', 'wind_speed': 2.5,
                    'wind_gust': 5.1, 'pressure_mm': 758, 'pressure_pa': 1010,
                    'humidity': 81, 'uv_index': 0, 'soil_temp': 16,
                    'soil_moisture': 0.31, 'prec_mm': 0, 'prec_period': 60,
                    'prec_prob': 0}],
         'biomet': {'index': 0, 'condition': 'magnetic-field_0'}
         }

]

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

DAY_PART = {'night': 'ночью', 'morning': 'утром', 'day': 'днем',
       'evening': 'вечером', 'fact': 'сейчас'}


def parse_data_for_days(data):
    forecast_for_days = []
    for day in data:
        forecast_for_days.append(day.get('date'))
        for part, weather in day['parts'].items():
            daypart = DAY_PART.get(part)
            temp_avg = weather.get('temp_avg')
            wind_speed = weather.get('wind_speed')
            wind_dir = weather.get('wind_dir')
            humidity = weather.get('humidity')
            feels_like = weather.get('feels_like')
            condition = weather.get('condition')
            forecast_for_part = (
                f'{daypart} температура воздуха - {temp_avg}°C'
                f'         (ощущается как - {feels_like}), '
                f'         {CONDITIONS[condition]}, '
                f'         скорость порывов ветра - {wind_speed}, '
                f'         направление ветра - {WIND_DIR[wind_dir]}, '
                f'         влажность воздуха {humidity}%. '
                f'')
            forecast_for_days.append(forecast_for_part)

    return forecast_for_days

print(parse_data_for_days(forecasts))