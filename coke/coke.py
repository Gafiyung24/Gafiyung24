#defining price of coke
def main():
    c = 50
    print("Amount Due: " , c)
    calc_change(c)

def calc_change(amount_due):
    n = int(input("Insert Coin: "))
    while n < c:
        c = c - n
        print("Amount Due: ", c)
    else:
        print("Changed Owed: " 0)
