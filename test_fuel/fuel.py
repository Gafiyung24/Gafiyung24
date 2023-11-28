def main():

    p = input("Fraction: ") #users to enter fraction here X/Y
    l = convert(p) * 100  #l is the percentage of fraction entered
    print(f"{guage(l)}")


def guage(l):
    if l <= 1:
        return f"E"
    elif 99 <= l <= 100:
        return f"F"
    elif 1 < l < 99:
        return f"{round(l)}%"
    else:
        convert()



def convert(f):
    while True:
        x = f.split("/")
        try:
            return (int(x[0])/int(x[1]))
        except (ValueError, ZeroDivisionError):
            pass


if __name__ == "__main__":
    main()

