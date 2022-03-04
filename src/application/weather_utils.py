"""Tools for get and processed current weather in Saint-Petersburg."""
import os
from datetime import datetime, timedelta

import requests

API_KEY = os.environ["API_KEY"]

TIME_DELTA = timedelta(hours=3)


def get_raw_weather_data() -> dict:
    """Get raw weather data from Openweathermap API.

    @return: raw weather data
    """
    lat = '59.9311'
    lon = '30.3609'
    api_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}' \
              f'&lon={lon}&appid={API_KEY}'
    response = requests.get(url=api_url)
    if response.status_code == 200:
        raw_data = response.json()
    else:
        raw_data = 'Ohh, error...'
    return raw_data


def timestamp_to_iso_date(timestamp: datetime.timestamp) -> str:
    dt_object = datetime.fromtimestamp(timestamp) + TIME_DELTA
    return dt_object.date().isoformat()


def timestamp_to_hour(timestamp: datetime.timestamp) -> str:
    dt_object = datetime.fromtimestamp(timestamp) + TIME_DELTA
    date = str(datetime.strptime(str(dt_object), '%Y-%m-%d %H:%M:%S'))
    return date.split()[-1]


def kelvin_to_celsius(kelvin_temp: float) -> int:
    t0 = 273.15
    return round(kelvin_temp - t0)


def create_weather_message() -> str:
    raw_weather = get_raw_weather_data()
    if isinstance(raw_weather, dict):
        current_date = timestamp_to_iso_date(raw_weather['dt'])
        weather_type = raw_weather['weather'][0]['main']
        weather_description = raw_weather['weather'][0]['description']
        current_temp = kelvin_to_celsius(raw_weather['main']['temp'])
        temp_feels_like = kelvin_to_celsius(raw_weather['main']['feels_like'])
        temp_min = kelvin_to_celsius(raw_weather['main']['temp_min'])
        temp_max = kelvin_to_celsius(raw_weather['main']['temp_max'])
        pressure = raw_weather['main']['pressure']
        humidity = raw_weather['main']['humidity']
        wind_speed = raw_weather['wind']['speed']
        wind_deg = raw_weather['wind']['deg']
        sunrise_hour = timestamp_to_hour(raw_weather['sys']['sunrise'])
        sunset_hour = timestamp_to_hour(raw_weather['sys']['sunset'])
        message = f"Current date: {current_date}, " \
                  f"weather type: {weather_type}, " \
                  f"weather description: {weather_description}, " \
                  f"current temperature: {current_temp} C, " \
                  f"temperature feels like: {temp_feels_like}  C, " \
                  f"minimum temperature: {temp_min} C, " \
                  f"maximum temperature: {temp_max} C, " \
                  f"pressure: {pressure} hPa, " \
                  f"humidity: {humidity} %, " \
                  f"wind speed: {wind_speed} meter/sec, " \
                  f"wind direction: {wind_deg} degrees, " \
                  f"sunrise hour: {sunrise_hour}, " \
                  f"sunset hour: {sunset_hour}"
        return message
    else:
        return 'Ohh, error...'
