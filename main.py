from halo import Halo

import color_clustering
import constants
import favorites
import graphs
import recommendation
import remote_operations
import utils

# Intialization
spinner_global_queries = Halo(text="Checking if data present...", spinner='growVertical')
spinner_global_queries.start()
utils.create_folders()
spinner_global_queries.succeed('Checking done!')

# Importing dataset
spinner_global_queries = Halo(text="Importing kaggle data...", spinner='growVertical')
spinner_global_queries.start()
remote_operations.import_csv()
spinner_global_queries.succeed('Datas imported!')

# Convert CSV data file to JSON format
spinner_global_queries = Halo(text="Converting CSV to JSON...", spinner='growVertical')
spinner_global_queries.start()
utils.csv_to_json(f'{constants.DATA_FOLDER}cards.csv', f'{constants.DATA_FOLDER}data.json')
spinner_global_queries.succeed('CSV file converted to JSON!')

# Download images found in JSON data file
spinner_global_queries = Halo(text="Downloading images...", spinner='growVertical')
spinner_global_queries.start()
remote_operations.download_images(nb_images=50) 
spinner_global_queries.succeed('Data and images successfully downloaded!')

# Analyze images main colors
spinner_global_queries = Halo(text="Analizing images colors...", spinner='growVertical')
spinner_global_queries.start()
color_clustering.get_colors()
spinner_global_queries.succeed('Images colors successfully analyzed!')

# Favorite input by user
spinner_global_queries = Halo(text="Generating manual favorites...", spinner='growVertical')
spinner_global_queries.start()
favorites.select_favorites(nb_favorites=10)
spinner_global_queries.succeed('Manual favorites generated!')

# Recommendation system
spinner_global_queries = Halo(text="Generating recommendations...", spinner='growVertical')
spinner_global_queries.start()
recommendation.recommend()
spinner_global_queries.succeed('Recommendations generated!')

# Graph display
spinner_global_queries = Halo(text="Displaying graphs...", spinner='growVertical')
spinner_global_queries.start()
graphs.show_graphs()
spinner_global_queries.succeed('Graphs displayed!')
