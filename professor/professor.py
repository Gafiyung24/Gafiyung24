import random


def main():



def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n <= 0 or n > 3:
                raise ValueError
        except ValueError:
            pass
        else:
            return n


def generate_integer(level):
    if level == 1:
    p = random.randrange(0,9)
    q = random.randrange(0,9)

    


if __name__ == "__main__":
    main()