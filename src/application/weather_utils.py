"""Tools for get and processed current weather in Saint-Petersburg."""
import requests
import os


API_TOKEN = os.environ["API_TOKEN"]


def get_raw_weather_data() -> dict:
    """Get raw weather data from Openweathermap API.

    @return: raw weather data
    """
    lat = '59.9311'
    lon = '30.3609'
    api_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}' \
              f'&lon={lon}&appid={API_TOKEN}'
    response = requests.get(url=api_url)
    if response.status_code == 200:
        raw_data = response.json()
    else:
        raw_data = 'Ohh, error...'
    return raw_data
