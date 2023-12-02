import sys
from tabulate import tabulate
import csv

def main():
    c = check_arg() #storing sys.argv in a variable after check
    if sys.argv[1] == "Sicilian.csv":
        l = csv_printer(c) #storing table in a variable
        print(l)
    elif sys.argv[1] == "Regular.csv":
        l = csv_printer2(c) #storing table in a variable
        print(l)

def check_arg():
    #check for condtions of command line argumemts
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command_line arguments")
    elif sys.argv[1].find(".csv") == -1:
        sys.exit("File doesn't exist")
    return sys.argv[1]

def csv_printer(n):#function to print csv talble
    pizzas = []
    try:
        with open(n, "r") as file:
            lines = csv.DictReader(file)
            for line in lines:
                pizzas.append({"Sicilian Pizza": line["Sicilian Pizza"], "Small": line["Small"], "Large": line["Large"]})
    except FileNotFoundError:
        sys.exit("File doesn't exist")
    else:
        pizza_table = tabulate(pizzas, headers = "keys", tablefmt = "grid")
        return pizza_table

def csv_printer2(n):#function to print csv talble regular pizza
    pizzas = []
    try:
        with open(n, "r") as file:
            lines = csv.DictReader(file)
            for line in lines:
                pizzas.append({"Regular Pizza": line["Regular Pizza"], "Small": line["Small"], "Large": line["Large"]})
    except FileNotFoundError:
        sys.exit("File doesn't exist")
    else:
        pizza_table = tabulate(pizzas, headers = "keys", tablefmt = "grid")
        return pizza_table




if __name__ == "__main__":
    main()
