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
