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
            if int(match.group(1)) > 12 or int(match.group(4)) > 12:
                raise ValueError
            elif int(match.group(2)) > 60 or int(match.group(5)) >60:
                raise ValueError
        except ValueError:
            sys.exit("Time entered is wrong")
        else:
            #converting input to output on how AM or PM was entered with time
            if match.group(3) == "AM" and match.group(6) == "AM":
                return f"{int(match.group(1)):02}:{int(match.group(2)):02} to {int(match.group(4)):02}:{int(match.group(5)):02}"
            elif match.group(3) == "AM" and match.group(6) == "PM":
                return f"{int(match.group(1)):02}:{int(match.group(2)):02} to {int(match.group(4))+12}:{int(match.group(5)):02}"
            elif match.group(3) == "PM" and match.group(6) == "AM":
                return f"{int(match.group(1))+12}:{int(match.group(2)):02} to {int(match.group(4)):02}:{int(match.group(5)):02}"
            elif match.group(3) == "PM" and match.group(6) == "PM":
                return f"{int(match.group(1))+12}:{int(match.group(2)):02} to {int(match.group(4))+12}:{int(match.group(5)):02}"
    else:
        sys.e







if __name__ == "__main__":
    main()
