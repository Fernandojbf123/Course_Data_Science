# -*- coding: utf-8 -*-
import weather_configs
import requests


def get_city_weather(city_name,country_code):
    url = weather_configs.URL + f"{city_name},{country_code}&appid={weather_configs.API_KEY}&lang=es"
    return requests.get(url)


