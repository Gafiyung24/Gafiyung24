import csv
import sys

def main():

def check():#function to check argument
    if len(sys.argv) < 3:
        sys.exit("Too few command line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command line arguments")

def csv_spliter(n):#function to split names in the csv file
    names = []
    try:
        with open(n, "r") as file:
            lines = csv.DictReader(file)
            for line in lines:
                names.append(line["name"].split(",")[0], line["house"])
    except FileNotFoundError:
        sys.exit(f"cannot read {n}")
    else:
        return names
def csv_writter(w, n2):#function to write name in new csv
    with open(n2, "a") as file:
        writer = csv.writer(file, fieldnames= "first", "last", )



if __name__ == "__main__":
    main()
