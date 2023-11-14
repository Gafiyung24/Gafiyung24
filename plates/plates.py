def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if check_alpha(s) and check_len(s) and check_last(s) and check_alnum(s): #for only alphabet and numbers
        t = True
    elif check_all_alpha(s) and check_len(s) and check_alpha(s):
        t = True
    else:
        t = False
    return t

def check_alpha(s):
    #function to check if first 2 digits are alphabets
    p = len(s)
    if 2 <= p <= 6:
        for i, c in enumerate(s):
            if s[0].isalpha() and s[1].isalpha():
                a = True
            else:
                a = False
        return a

def check_len(s):
    #fuction to check if length of plate is within 2 and 6 digits
    p = len(s)
    if 2 <= p <= 6:
        p = True
    else:
        p = False
    return p


def check_last(s):
    #fuction to make suure the last digit is a number and first digit is not zero
    if s.isalnum():
        for i, c in enumerate(s):
            if s[i].isnumeric() and s[i+1:].isnumeric() and s[i] != "0":
                p = True
            else:
                p = False
        return p

def check_alnum(s):
    if s.isalnum() is True:
        return True

def check_all_alpha(s):
    if s.isalpha():
        p = False
    else:
        p = True
    return p


main()

