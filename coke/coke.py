#defining price of coke
def main():
    c = 50
    print("Amount Due: " , c)
    calc_change()

def calc_change(amount_due):
    n = int(input("Insert Coin: "))
    while n < 50:
        c = 50 - n
        print("Amount Due: ", c)
    else:
        c = 0
        print("Changed Owed: ", c)
return c

main()
