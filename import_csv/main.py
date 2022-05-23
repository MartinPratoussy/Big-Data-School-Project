from importlib import resources
import os
from halo import Halo
import shutil

import constants
import remote_operations
import utils

if os.path.exists("Resources/states"):
    shutil.rmtree("Resources/states")

# Intialization
spinner_global_queries = Halo(text="Checking if data present...", spinner='growVertical')
spinner_global_queries.start()
utils.create_folders()
spinner_global_queries.succeed('Checking done!')

# Importing dataset
spinner_global_queries = Halo(text="Importing kaggle data...", spinner='growVertical')
spinner_global_queries.start()
remote_operations.import_csv()
spinner_global_queries.succeed('Data imported!')

# Convert CSV data file to JSON format
spinner_global_queries = Halo(text="Converting CSV to JSON...", spinner='growVertical')
spinner_global_queries.start()
utils.csv_to_json(f'{constants.DATA_FOLDER}cards.csv', f'{constants.DATA_FOLDER}data.json')
spinner_global_queries.succeed('CSV file converted to JSON!')

# Download images found in JSON data file
spinner_global_queries = Halo(text="Downloading images...", spinner='growVertical')
spinner_global_queries.start()
remote_operations.download_images(nb_images=20) 
spinner_global_queries.succeed('Data and images successfully downloaded!')

os.mkdir("Resources/states")
with open('Resources/states/import.txt', 'w') as f:
    f.write('Done!')