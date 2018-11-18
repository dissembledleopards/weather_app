# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 15:10:29 2018

@author: sarah
"""

#city = input("City?")


import json
import requests
import random

# get base url and api key from file
def get_api_key():
    with open("url_key.txt", "r") as f:
        url_key = f.read()
    url_key = url_key.split("\n")
    return url_key

 # call api to get weather data
def call_api(city, units="metric"):
    api_key, base_url = get_api_key()
    parameters = "&q=%s&units=%s" % (city, units)
    response = requests.get(base_url+api_key+parameters)
    data = response.json()
    return data

# ask user whether to run for Leeds or select different city. Return choice of city
def choose_city():
    city_choice = input("Weather for Leeds? (Any key to run or c to change city) \n")
    if city_choice.lower() == "c":
        city_choice = input("Enter a city\n")
    else:
        city_choice = "Leeds"
    return city_choice

# generate weather forecast description from data
def generate_forecast(api_data, city, a):
    city_weather = api_data["list"][a]
    weather_description = city_weather["weather"][0]["description"]
    temp_main = city_weather["main"]["temp"]
    temp_min = city_weather["main"]["temp_min"]
    temp_max = city_weather["main"]["temp_max"]
    time_ref = "Current temperature"
    etre_phrase = "\'s"
    #if a == 0:
     #   time_ref = "Current temperature"
      #  etre_phrase = "\'s"
    #else:
    #    time_ref = "The weather for %s until %s" % (weather_info["list"][0]["dt_txt"], weather_info["list"][a + 1]["dt_txt"])
    #    etre_phrase = " will be"
    temperature = "%s in %s is %s\u00B0C, with a high of %s\u00B0C and a low of %s\u00B0C. Pretty sure it%s %sing" % (time_ref, city.title(), temp_main, temp_max, temp_min, etre_phrase, weather_description)
    print(temperature)
    
    
def get_forecast():
    a = 0
    while True:
        generate_forecast(a)
        user_response = input(random.choice(["Get the next three hours?\n", "And another three hours?\n", "Once more?\n", "Get my next prediction?\n", "Get the next three hours?\n"]))
        if user_response.lower() == "n" or user_response.lower() == "no":
            run_or_change = input("Run again (y) or exit (any other key)?\n")
            if run_or_change.lower() == "y":
                a = 0
            else:
                print("Have a nice day :)")
                return
        else:
            a += 1
            
def main():
    city = choose_city()
    api_data = call_api(city)
    generate_forecast(api_data, city)
    get_forecast()
        
    # ask city
    # call get forecast for that city
    # get forecast - get weather data for city, iterates data asking user
            
            
# "More weather for %s?\n" % (city_name)