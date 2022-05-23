import os
import zipfile
import json
import requests

import constants

def import_csv():
    os.system('kaggle datasets download -d ioexception/yugioh-cards')
    with zipfile.ZipFile('yugioh-cards.zip', 'r') as zip_ref:
        zip_ref.extractall(f'{constants.DATA_FOLDER}')
    os.remove('yugioh-cards.zip')

def download_images(nb_images=20):
    with open(f'{constants.DATA_FOLDER}data.json', 'r') as f:
        cards_dict = json.load(f)
        for card, _ in zip(cards_dict, range(nb_images)):
            try:
                card_img = requests.get(card['image_url']).content
                with open(f"{constants.IMAGES_FOLDER}{card['id']}.jpg",'wb') as f:
                    f.write(card_img)
            except requests.exceptions.RequestException as e:
                print(e)