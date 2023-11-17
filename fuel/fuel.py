def main():
    l = get







def get_level():
    while True:
        x = input("Fraction: ").split("/")
        try:
            return int(x[0])/int(x[1])
        except (ValueError, ZeroDivisionError)
            pass



main()

