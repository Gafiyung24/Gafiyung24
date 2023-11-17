"""input("What is your name? :")
print("hello, World")
print("meow\n" * 3, end= "")
def main():
    print_column(3)



def print_column(height):
    for _ in range(height):
        print("#" * 3)"""

def main():
    g = input("fraction: ").split("/")
    print(f"{divide(g)}")


def divide(x):
    x_d = x[0] / x[1]
    return x_d
main()






