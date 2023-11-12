"""input("What is your name? :")
print("hello, World")
print("meow\n" * 3, end= "")"""
def main():
    n = print_column(3)
    print(f"{n}*3")


def print_column(height):
    for _ in range(height):
        print("#")


main()
