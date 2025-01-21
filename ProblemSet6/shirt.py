import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) == 3:
    extension = [".jpeg",".jpg",".png"]
    extension1 = os.path.splitext(sys.argv[1])
    extension2 = os.path.splitext(sys.argv[2])
    if extension1[1] == extension2[1] and extension1 in extension:
        try:
            user_image = Image.open(sys.argv[1])


        except FileNotFoundError:
            sys.exit("File doesn't exist")
user_image = Image.open(sys.argv[1])
shirt = Image.open("shirt.png")
size = shirt.size
user_image = ImageOps.fit(user_image, size)
user_image.paste(shirt, shirt)
user_image.save(sys.argv[2])

if len(sys.argv) > 3:
    sys.exit("Too many command-line argument")
if len(sys.argv) < 3:
    sys.exit("Too few command-line argument")

