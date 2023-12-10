import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    #find match for pattern 9:00 AM to 5:00PM with regex
    match = re.search(r"^([0-9]+):([0-9]+) {1}(AM|PM) {1}to {1}([0-9]+):([0-9]+) {1}(AM|PM)$", s)
    if match:
        #conditionals to make sure input meets specified criteria
        try:
            if int(match.group(1))






if __name__ == "__main__":
    main()
