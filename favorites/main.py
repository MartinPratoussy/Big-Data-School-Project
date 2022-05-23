from time import sleep
from halo import Halo
import os

import favorites

while not os.path.exists(path="Resources/states/colors.txt"):
    sleep(1)

# Favorite input by user
spinner_global_queries = Halo(text="Generating manual favorites...", spinner='growVertical')
spinner_global_queries.start()
favorites.random_favorites()
spinner_global_queries.succeed('Manual favorites generated!')

with open('Resources/states/favorites.txt', 'w') as f:
    f.write('Done!')