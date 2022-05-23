import csv 
import json
import os
import shutil

import constants

def create_folders():
    if os.path.isdir(f'{constants.RESOURCES_FOLDER}') and os.path.isdir(f'{constants.IMAGES_FOLDER}'):
        shutil.rmtree(f'{constants.RESOURCES_FOLDER}')
    os.makedirs(f'{constants.IMAGES_FOLDER}')
    os.makedirs(f'{constants.DATA_FOLDER}')

# CSV to JSON converter took from https://pythonexamples.org/python-csv-to-json/#2
def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
  
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)

def rgb_to_hex(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))

#function to find Yu-Gi-Oh! card by id in json         
def find_by_id(json, value):
    return next((data for data in json if data['id']==value), None)

#function to find Yu-Gi-Oh! card by id in json         
def find_by_name_analyzed(json, value):
    return next((data for data in json['data'] if str(data['id']) == value), False)

def chunks(list, n):
    n = max(1, n)
    return (list[i : i + n] for i in range(0, len(list), n))
