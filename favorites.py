from PIL import ImageTk, Image
import tkinter as tk
import json
import random

import constants

FAVORITE_DATA=[]

def select_favorites(nb_favorites=20):
    with open(f'{constants.DATA_FOLDER}{constants.ANALYZED_DATA}') as json_file:
        json_file = json.load(json_file)['data']
    for _ in range(nb_favorites):
        random_yu_gi_oh_card = random.randint(0, len(json_file)-1)
        show_tk_windows(json_file[random_yu_gi_oh_card])

    with open(f'{constants.DATA_FOLDER}{constants.FAVORITES_DATA}', 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(FAVORITE_DATA, indent=4)
        jsonf.write(jsonString)

def show_tk_windows(data):
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()

    button1 = tk.Button(frame, text="Like", fg="green",
                        command=lambda: save_score(root, data, 1))
    button2 = tk.Button(frame, text="Dislike", fg="red",
                        command=lambda: save_score(root, data, -1))

    button1.pack(side=tk.LEFT)
    button2.pack(side=tk.RIGHT)

    img = ImageTk.PhotoImage(Image.open(f"{constants.IMAGES_FOLDER}" +
                                        str(data['id']) + ".jpg"))
    panel = tk.Label(frame, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    root.mainloop()

def save_score(window, data, score):
    analyzed_object = {}
    analyzed_object.update(data)
    if(any(favorite_data["id"] == data["id"] for favorite_data in FAVORITE_DATA)):
        exist_object = next(
            obj for obj in FAVORITE_DATA if obj['id'] == data['id'])
        exist_object['score'] = exist_object['score'] + \
            score if 'score' in exist_object else score
        FAVORITE_DATA.append(exist_object)
    else:
        analyzed_object['score'] = analyzed_object['score'] + \
            score if 'score' in analyzed_object else score
        FAVORITE_DATA.append(analyzed_object)
    window.destroy()