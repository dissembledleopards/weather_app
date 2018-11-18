# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 18:03:41 2018

@author: sarah
"""

with open("city_list.json","rb") as cities_file:
    jsondata = json.load(cities_file)
    
def create_cities_dict():
    city_names_li = []
    country_id_li = []
    for i in range(len(jsondata)):
        city_names_li.append(jsondata[i]["name"])
    for i in range(len(jsondata)):
        country_id_li.append(jsondata[i]["id"])
    cities_codes_dict = {}
    for i in range(len(city_names_li)):
        cities_codes_dict[city_names_li[i]] = country_id_li[i]
    return cities_codes_dict

fetch_id = cities_codes_dict[user_city]