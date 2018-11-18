# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 21:51:15 2018

@author: sarah
"""


# city codes dict 1: open json containing city names and codes
def get_cities_json():
    with open("city_list.json","rb") as cities_file:
        json_data = json.load(cities_file)
    return json_data
    
# city codes dict 2: create dict name : code from json data
def get_city_code(json_data):
    city_names_li = []
    country_id_li = []
    cities_codes_dict = {}
    for i in range(len(json_data)):
        city_names_li.append(json_data[i]["name"])
        country_id_li.append(json_data[i]["id"])
    for i in range(len(city_names_li)):
        cities_codes_dict[city_names_li[i]] = country_id_li[i]
    return cities_codes_dict

# call city codes dict 1 + 2 to return city code for an inputted city name
def return_city_code():
    json_data = get_cities_json()
    cities_codes_dict = get_city_code(json_data)
    return cities_codes_dict[input("City?\n")]