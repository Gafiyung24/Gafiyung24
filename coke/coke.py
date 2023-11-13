#defining price of coke
def main():
    c = 50
    print("Amount Due: " , c)
    calc_change()

def calc_change():
    i = 0
    while i < 50:
        n = int(input("Insert Coin: "))

        if n == 5 | 10 | 25:
            i = n + i

            if i < 50:
                print("Amount Due:", 50-i)
            else:
                print("Change Owed:", i-50)
        else:
            print("Amount Due:", 50)
            i = 50
main()

