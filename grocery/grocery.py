def main():


def list():

    my_list = []
    while True:
        try:
            my_list.append(input().upper())
        except KeyError:
            pass
        except EOFError:
            return my_list.sort()



main()
