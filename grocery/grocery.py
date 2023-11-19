def main():


def arrange():#fuction to get userinput and append to list

    my_list = []
    while True:
        try:
            my_list.append(input().upper())
        except KeyError:
            pass
        except EOFError:
            return my_list.sort()



main()
