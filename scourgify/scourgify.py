import csv
import sys

def main():
    check()
    list_names = csv_spliter(sys.argv[1])
    csv_writter(list_names,sys.argv[2])

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
                names.append([line["name"].strip().split(",")[0],line["name"].strip().split(",")[1], line["house"]])
    except FileNotFoundError:
        sys.exit(f"cannot read {n}")
    else:
        return names
def csv_writter(w, n2):#function to write name in new csv
    with open(n2, "a") as file:
        writer = csv.DictWriter(file, fieldnames= ["first", "last", "house"])
        writer.writeheader()
        for ls in w:
            writer.writerow({"first":ls[0],"last":ls[1],"house":ls[2]})

if __name__ == "__main__":
    main()
