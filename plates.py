def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    ...
def check_alpha(s):
    for i, c in enumerate(s):
        if s[0].isalpha() and s[1].isalpha():
            return True
def check_len(s):
    p = len(s)
    if 2 <= p <= 6:
        return True
def check_last(s):
    for i, c in enumerate(s):
        if s[i].isnumeric() and s[i+1].isnumeric()

main()
