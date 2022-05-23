from PIL import ImageTk, Image
import tkinter as tk
import json
import random

import constants

def random_favorites():
    with open(f'{constants.DATA_FOLDER}{constants.ANALYZED_DATA}') as json_file:
        json_file = json.load(json_file)['data']
    new_data=[]
    for data in json_file:
        new_object={}
        new_object.update(data)
        m=random.randint(0,3)
        if m==0:
            n = random.randint(0,5)
            new_object['score']=n
        else:
            new_object['score']=""
        new_data.append(new_object)
    with open(f'{constants.DATA_FOLDER}{constants.FAVORITES_DATA}', 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(new_data, indent=4)
        jsonf.write(jsonString)