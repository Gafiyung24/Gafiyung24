#defining price of coke
def main():
    c = 50
    print("Amount Due: " , c)
    calc_change()

def calc_change():
    i = 0
    while i < 50:
        n = int(input("Insert Coin: ").strip())
        i = n + i

        if n != 5 or 10 or 25:


            if i < 50:
                print("Amount Due:", 50-i)
            elif i >= 50:
                print("Change Owed:", i-50)
        else:
            print("Amount Due:", 50)

main()

