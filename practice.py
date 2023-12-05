import csv
import sys

#function to split names in the csv file
names = []
try:
    with open("scourgify/before.csv", "r") as file:
        lines = csv.DictReader(file)
        for line in lines:
            names.append([line["name"].strip().split(",")[0], line["name"].strip().split(",")[1], line["house"]])
except FileNotFoundError:
    sys.exit(f"cannot read")
else:
    print(names)


'''def paste(n1, n2):
    im_shirt = Image.open("shirt.png")
    size = im_shirt.size
    #mask = im_shirt.convert("L")
    #mask = im_shirt.split()[3]
    try:
        with Image.open(n1) as im1:
            ImageOps.fit(im1, size).save(n2)
    except OSError:
        sys.exit("File can't be opened")
    else:
        with Image.open(n2) as im2:
            im2.paste(im_shirt, im_shirt)
            return im2.save(n2)
'''
