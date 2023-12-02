import csv
import sys
def csv_spliter(n):#function to split names in the csv file
    names = []
    try:
        with open(n, "r") as file:
            lines = csv.DictReader(file)
            for line in lines:
                names.append([line["name"].strip().split(",")[0], line["house"]])
    except FileNotFoundError:
        sys.exit(f"cannot read {n}")
    else:
        return names
