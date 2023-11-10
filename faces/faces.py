def main():


    userinput = input("Enter something:")
    convert(userinput)


def convert(m):
    m = m.replace(':)', '🙂').replace(':(', '🙁')
    print(m)


main()




