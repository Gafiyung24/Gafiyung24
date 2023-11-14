def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if check_alpha(s) and check_len(s) and check_last(s) and check_alnum(s):
        return True

def check_alpha(s):
    #function to check if first 2 digits are alphabets
    for i, c in enumerate(s):
        if s[0].isalpha() and s[1].isalpha():
            return True

def check_len(s):
    #fuction to check if length of plate is within 2 and 6 digits
    p = len(s)
    if 2 <= p <= 6:
        return True

def check_last(s):
    #fuction to make suure the last digit is a number
    for i, c in enumerate(s):
        if s[i].isnumeric() and s[i+1:].isnumeric():
            return True

def check_alnum(s):
    if s.isalnum() is True:
        return True


main()
