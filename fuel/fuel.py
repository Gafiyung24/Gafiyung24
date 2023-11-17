def main():
    l = get_level() * 100

    if l <= 1:
        print("E")
    elif l >= 99:
        print("F")
    elif 1 < l < 99:
        print(f"{l}%")
    else:
        get_level()



def get_level():
    while True:
        x = input("Fraction: ").split("/")
        try:
            return (int(x[0])/int(x[1]))
        except (ValueError, ZeroDivisionError):
            pass



main()

