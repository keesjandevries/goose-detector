from sys import argv
from PIL import Image
import os
import time

TARGET = "car"
paths_file_name = argv[1]
label_dir = argv[2]

with open(paths_file_name) as f:
    paths = f.read().splitlines()

def show_image(path, sleep_time):
    image = Image.open(path)
    image.show()
    image.close()

for path in paths:
    label_path = os.path.join(label_dir, os.path.split(path)[1]) 
    print(label_path)
    if os.path.exists(label_path):
        print("File already exists: {label_path}".format(label_path=label_path))
        pass
    else:
        show_image(path, 5)
        label = input("Is there a {target} in this image? y/n/?\n".format(target=TARGET))
        while(not(label=="y" or label=="n")):
            show_image(path, 5)
            label = input("Please reply 'y' or 'n'. Is this a {target}?".format(target=TARGET))
        with open(label_path, "w") as label_file:
            label_file.write(str(int(label=="y")))
