import sys
from tabulate import tabulate
import csv

def main():

def check_arg():
    #check for condtions of command line argumemts
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command_line arguments")
    elif sys.argv[1].find(".py") == -1:
        sys.exit("File doesn't exist")
    return sys.argv[1]

def csv_printer():
    




if __name__ == "__main__":
    main()
