# -*- coding: utf-8 -*-

import data
import sender_stand_request


response = sender_stand_request.get_city_weather(data.city_name,data.country_code).json()

weather = response["weather"][0]["description"]
temperature = response["main"]["temp"]-273.15
wind_speed = response["wind"]["speed"]
wind_dir = response["wind"]["deg"]

print(f"The weater in {data.city_name} is:")
print(f"{weather}")
print(f"with a temperature of {temperature:.2f} ºC")
print(f"wind speed of {wind_speed:.2f} m/s")
print(f"and wind direction {wind_dir:.2f} degrees")