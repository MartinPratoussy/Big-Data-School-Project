from time import sleep
from halo import Halo
import os.path
from os import path

import color_clustering

while not os.path.exists(path="Resources/states/import.txt"):
    sleep(1)

# Analyze images main colors
spinner_global_queries = Halo(text="Analizing images colors...", spinner='growVertical')
spinner_global_queries.start()
color_clustering.get_colors()
spinner_global_queries.succeed('Images colors successfully analyzed!')

with open('Resources/states/colors.txt', 'w') as f:
    f.write('Done!')