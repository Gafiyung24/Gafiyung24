#defining price of coke
def main():
    c = 50
    calc_change()

def calc_change(amount_due):
    n = int(input("Insert Coin: "))
    while n < c:
        c = c - n
        print()


