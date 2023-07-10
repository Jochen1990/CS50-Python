import sys
import os
from PIL import Image, ImageOps


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

elif sys.argv[1].endswith(".jpeg") != True and sys.argv[1].endswith(".png") != True and sys.argv[1].endswith(".jpg") != True:
    sys.exit("please choose correct fromat")

elif sys.argv[2].endswith(".jpeg") != True and sys.argv[2].endswith(".png") != True and sys.argv[2].endswith(".jpg") != True:
    sys.exit("Invalid Input")

elif os.path.splitext(sys.argv[1])[1] != os.path.splitext(sys.argv[2])[1]:
    sys.exit("Input and output have different extensions")

else:
    try:
        with Image.open(sys.argv[1]) as image, Image.open("shirt.png") as shirt:
            modified_image = ImageOps.fit(image, (shirt.size))
            modified_image.paste(shirt, shirt)
            modified_image.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("Files do not exist")