import json
from tkinter import *
from tkinter import ttk
from turtle import color
from PIL import ImageTk, Image
from halo import Halo

from cv2 import COLOR_BGR2BGR555

import constants

def recommend():
    with open(f'{constants.DATA_FOLDER}{constants.FAVORITES_DATA}') as favorites_file:
        favorites_file = json.load(favorites_file)

    with open(f'{constants.DATA_FOLDER}{constants.ANALYZED_DATA}') as json_file:
        json_file = json.load(json_file)

    recommended_data = []

    for data in favorites_file:
        if data["score"] not in ["", 0]:
            score = int(data["score"])
            for data_to_recommend in json_file["data"]:

                spinner_global_queries = Halo(text='Rating ' + str(data_to_recommend["id"]) + '...', spinner='growVertical')
                spinner_global_queries.start()
                rating = calculate_recommend(data, data_to_recommend)
                spinner_global_queries.succeed(str(data_to_recommend["id"]) + ' rated!')

                if rating != 0:
                    new_object = {}
                    new_object.update(data_to_recommend)
                    new_object["recommendation"] = rating
                    recommended_data.append(new_object)

    with open(f'{constants.DATA_FOLDER}{constants.RECOMMENDED_DATA}', 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(recommended_data, indent=4)
        jsonf.write(jsonString)

def calculate_recommend(data, data_to_recommend):
    rating = 0
    if data["archetype"] == data_to_recommend["archetype"]:
        rating += 20
    if data["attribute"] == data_to_recommend["attribute"]:
        rating += 20
    if data["race"] == data_to_recommend["race"]:
        rating += 15
    if data["type"] == data_to_recommend["type"]:
        rating += 15
    if data["color1"] == data_to_recommend["color1"]:
        rating += 14
    if data["color1"] == data_to_recommend["color2"]:
        rating += 7
    if data["color2"] == data_to_recommend["color2"] or data["color1"] == data_to_recommend["color3"]:
        rating += 3
    if data["color2"] == data_to_recommend["color3"]:
        rating += 2
    if data["color3"] == data_to_recommend["color3"]:
        rating += 1

    return rating
