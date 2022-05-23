from audioop import reverse
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import json
import numpy as np

import constants
import utils

def show_graphs():
    with open(f'{constants.DATA_FOLDER}{constants.RECOMMENDED_DATA}') as json_file:
        json_file = list(json.load(json_file))
    json_file.sort(key=lambda x: x["recommendation"], reverse=True)
    splitted = list(utils.chunks(json_file,10))
    i=1
    for chunk in splitted:
        display(chunk,splitted,i)
        i+=1

def display(chunk,splitted,i):
    names = []
    rec = []
    fig, ax = plt.subplots()
    for data in chunk:
        names.append(plt.imread(f"{constants.IMAGES_FOLDER}" + str(data['id']) + ".jpg"))

        rec.append(data['recommendation'])
    y_pos = np.arange(len(names))
    ax.set_xlabel('Percentage')
    ax.set_title(f'Recommendations ({str(i)}/{len(list(splitted))})')
    ax.invert_yaxis()
    ax.barh(y_pos, rec, align='center')
    ax.set_yticks(y_pos, labels="")
    tick_labels = ax.yaxis.get_ticklabels()
    for i,im in enumerate(names):
        ib = OffsetImage(im, zoom=.05)
        ib.image.axes = ax
        ab = AnnotationBbox(ib,
                        tick_labels[i].get_position(),
                        frameon=False,
                        box_alignment=(1, 0.5)
                        )
        ax.add_artist(ab)
    plt.show()
