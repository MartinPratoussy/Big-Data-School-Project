import os
from time import sleep
from halo import Halo

import recommendation

while not os.path.exists(path="Resources/states/favorites.txt"):
    sleep(1)

# Recommendation system
spinner_global_queries = Halo(text="Generating recommendations...", spinner='growVertical')
spinner_global_queries.start()
recommendation.recommend()
spinner_global_queries.succeed('Recommendations generated!')

with open('Resources/states/recommendations.txt', 'w') as f:
    f.write('Done!')