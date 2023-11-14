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
        if i[0].alpha() and i[1].alpha():
            return True
def check_len(s):
    p = len(s)
    if 2 <= p <= 6:
        return True
def check_last(s):
    for i, 

main()
