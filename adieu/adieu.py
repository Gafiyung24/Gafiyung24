import inflect

p = inflect.engine()
mylist = []
while True:
    try:
        mylist.append(input("Name: "))
    except EOFError:
        print()

