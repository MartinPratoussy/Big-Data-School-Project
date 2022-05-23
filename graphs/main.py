import os
from time import sleep
from halo import Halo

import graphs

while not os.path.exists(path="Resources/states/recommendations.txt"):
    sleep(1)

# Graph display
spinner_global_queries = Halo(text="Displaying graphs...", spinner='growVertical')
spinner_global_queries.start()
#graphs.show_graphs()
spinner_global_queries.succeed('Graphs displayed!')
