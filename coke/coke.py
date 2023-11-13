#defining price of coke
def main():
    c = 50
    calc_change()

def calc_change(amount_due):
    n = int(input("Insert Coin: "))
    while n < c:
        n = c - n
        


