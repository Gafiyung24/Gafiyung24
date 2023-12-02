import csv
import sys

def main():

def check():#function to check argument
    if len(sys.argv) < 3:
        sys.exit("Too few command line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command line arguments")

def csv_spliter(n):
    names = []
    try:
        with open(n, "r") as file:
            lines = csv.DictReader(file)
            for line in lines:
                names.append(line["name"].split(",")[0], line["house"])
    except FileNotFoundError:
        sys.exit(f"cannot read {n}" )


if __name__ == "__main__":
    main()
