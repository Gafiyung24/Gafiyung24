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

        if n != 5 and n!= 10 and n !=25:
            print("Amount Due:", 50)
            break
        elif i < 50:
            print("Amount Dues:", 50-i)
        else:
            print("Change Owed:", i-50)


main()

