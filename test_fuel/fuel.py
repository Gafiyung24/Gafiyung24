def main():
    l = get_level() * 100
    p = input("Fraction: ") #users to enter fraction here X/Y

def guage()
    if l <= 1:
        print("E")
    elif 99 <= l <= 100:
        print("F")
    elif 1 < l < 99:
        print(f"{round(l)}%")
    else:
        get_level()



def get_level(f):
    while True:
        x = f.split("/")
        try:
            return (int(x[0])/int(x[1]))
        except (ValueError, ZeroDivisionError):
            pass


if __name__ == "__main__":
    main()

