import sys
def main():

    p = input("Fraction: ") #users to enter fraction here X/Y
    l = convert(p) * 100  #l is the percentage of fraction entered
    print(f"{gauge(l)}")


def gauge(l):
    if l <= 1:
        return f"E"
    elif 99 <= l <= 100:
        return f"F"
    elif 1 < l < 99:
        return f"{round(l)}%"



def convert(f):
    x = f.split("/")
    if int(x[1]) == 0:
        raise ZeroDivisionError
    elif int(x[0]).isnumeric or int(x[1]).isnumeric == False:
        raise ValueError
    elif int(x[0]) > int(x[1]):
        raise ValueError

    return int(x[0])/int(x[1])




if __name__ == "__main__":
    main()

