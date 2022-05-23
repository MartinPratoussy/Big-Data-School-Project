import json
import os
from sklearn.cluster import KMeans
from collections import Counter
from webcolors import normalize_hex, hex_to_rgb
from tqdm import tqdm
import cv2
from halo import Halo

from classes import ColorNames

import constants
import utils

def get_colors(nb_colors=4):
    images = sorted(os.listdir(constants.IMAGES_FOLDER))

    data = {'data': []}
    for file_path in tqdm(images):
        colors = {'id': file_path.rsplit(".")[0]}
        spinner = Halo(text='Analyzing ' + colors['id'], spinner='growVertical')

        image = cv2.imread(f'{constants.IMAGES_FOLDER}{file_path}')
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        resized_image = resize_image(image)

        hex_colors = cluster_colors(resized_image, nb_colors)

        colors['colors'] = []
        for i in hex_colors:
            normalize_hex_str = normalize_hex(i)
            rgb = hex_to_rgb(normalize_hex_str)
            try:
                colors['colors'].append(ColorNames.findNearestWebColorName(rgb))
            except ValueError:
                print("Invalid number detected...")
        colors['color1'] = colors['colors'][1]
        colors['color2'] = colors['colors'][2]
        colors['color3'] = colors['colors'][3]
        data['data'].append(colors)

        spinner.succeed(colors['id']+' analyzed!')
        
    store_colors(data)

def resize_image(image):
        scale_percent = 60
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        
        resized_image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
        resized_image = resized_image.reshape(resized_image.shape[0] * resized_image.shape[1], 3)

        return resized_image

def cluster_colors(resized_image, nb_colors):
        clf = KMeans(n_clusters=nb_colors)
        labels = clf.fit_predict(resized_image)
        counts = Counter(labels)
        center_colors = clf.cluster_centers_

        ordered_colors = [center_colors[i] for i in counts.keys()]
        hex_colors = [utils.rgb_to_hex(ordered_colors[i]) for i in counts.keys()]

        return hex_colors

def store_colors(data):
    spinner = Halo(text='Updating JSON file...', spinner='growVertical')
    new_data = {'data': []}
    with open(f'{constants.DATA_FOLDER}data.json') as json_file:
        json_decoded = json.load(json_file)
    for element in data['data']:
        new_element = utils.find_by_id(json_decoded, element['id'])
        if new_element is not None:
            new_element['colors'] = element['colors']
            new_element['color1'] = element['color1']
            new_element['color2'] = element['color2']
            new_element['color3'] = element['color3']
            new_data['data'].append(new_element)
    with open(f'{constants.DATA_FOLDER}{constants.ANALYZED_DATA}', 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(new_data, indent=4)
        jsonf.write(jsonString)

    spinner.succeed('JSON file updated!')