# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 20:46:26 2018

@author: sarah
"""

import json
import requests
import random

    
def get_city_code():
    with open("city_list.json","rb") as cities_file:
        jsondata = json.load(cities_file)
    city = input("City?")
    city_names_li = []
    country_id_li = []
    cities_codes_dict = {}
    for i in range(len(jsondata)):
        city_names_li.append(jsondata[i]["name"])
        country_id_li.append(jsondata[i]["id"])
    for i in range(len(city_names_li)):
        cities_codes_dict[city_names_li[i]] = country_id_li[i]
    return cities_codes_dict[city]


def get_weather_info(units="metric"):
    api_key = "a17db140afba5204d477008140599531"
    base_url = "http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID="
    parameters = "&q=%s&units=%s" % (change_city(), units)
    response = requests.get(base_url+api_key+parameters)
    data = response.json()
    return data

def change_city():
    fetch_weather = input("Weather for Leeds? (Any key to run or c to change city) \n")
    if fetch_weather.lower() == "c":
        user_city = input("Enter a city\n")
    else:
        user_city = "Leeds"
    return user_city

    
def weather_forecast():
    weather_info = get_weather_info()
    city_name = weather_info["city"]["name"]
    a = 0
    while True:
        city_weather = weather_info["list"][a]
        weather_description = city_weather["weather"][0]["description"]
        temp_main = city_weather["main"]["temp"]
        temp_min = city_weather["main"]["temp_min"]
        temp_max = city_weather["main"]["temp_max"]
        if a == 0:
            time_ref = "Current temperature"
            etre_phrase = "\'s"
        else:
            time_ref = "The weather for %s until %s" % (weather_info["list"][a]["dt_txt"], weather_info["list"][a + 1]["dt_txt"])
            etre_phrase = " will be"
        temperature = "%s in %s is %s\u00B0C, with a high of %s\u00B0C and a low of %s\u00B0C. Pretty sure it%s %sing" % (time_ref, city_name, temp_main, temp_max, temp_min, etre_phrase, weather_description)
        print(temperature)
        user_response = input(random.choice(["Get the next three hours?\n", "And another three hours?\n", "Once more?\n", "More weather for %s?\n" % (city_name), "Get my next prediction?\n", "Get the next three hours?\n"]))
        if user_response.lower() == "n" or user_response.lower() == "no":
            run_or_change = input("Run again (y) or exit (any other key)?\n")
            if run_or_change.lower() == "y":
                return True
            else:
                print("Have a nice day :)")
                return False
        else:
            a += 1

def main():
    running = True
    while running:
        running = weather_forecast()

if __name__ == "__main__":
    main()
