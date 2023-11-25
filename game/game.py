import random


def main():

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


main()
