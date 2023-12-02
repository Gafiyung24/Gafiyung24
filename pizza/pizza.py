import sys
from tabulate import tabulate
import csv

def main():
    l = csv_printer()
    print(l)


"""def check_arg():
    #check for condtions of command line argumemts
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command_line arguments")
    elif sys.argv[1].find(".csv") == -1:
        sys.exit("File doesn't exist")
    return sys.argv[1]"""

def csv_printer():
    pizzas = []
    try:
        with open("pizza/sicilian.csv", "r") as file:
            lines = csv.DictReader(file)
            for line in lines:
                pizzas.append({"Sicilian Pizza": line["Sicilian Pizza"], "Small": line["Small"], "Large": line["Large"]})
    except FileNotFoundError:
        sys.exit("File doesn't exist")
    else:
        #for line in lines:
           # pizzas.append({"Sicilian": line["Sicilian"], "Small": line["Small"], "Large": line["Large"]})
        #for pizza in pizzas:

        pizza_table = tabulate(pizzas, headers = "keys", tablefmt = "grid")
        return pizza_table




if __name__ == "__main__":
    main()
