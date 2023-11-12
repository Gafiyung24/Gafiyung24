"""input("What is your name? :")
print("hello, World")
print("meow\n" * 3, end= "")
def main():
    print_column(3)



def print_column(height):
    for _ in range(height):
        print("#" * 3)


main()
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print("#" * size)

main()"""
user_input = input("name: ")
for i in user_input:
    if user_input[i].isupper() is True:
        output = user_input[:i-1] + "_"
    else:
        output = user_input
print(output)
