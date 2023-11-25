import random


def main():
    l, g = check()
    game(l, g)

def check():
    while True:
        try:
            n = int(input("level: "))
            i = int(input("Guess: "))
            if n or i < 0:
                raise ValueError
        except ValueError:
            pass
        else:
            c = random.choice(1, n)
            return c, i
def game(a, b):
    if a < b:
        print("Too small")
    elif a > b:
        print("Too large")
    else:
        print("Just right")


main()
