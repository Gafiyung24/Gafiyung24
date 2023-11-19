def main():
    d_list = {}
    user_input = sorted(list())
    for item in user_input:
        counter = d_list.get(item, 0)
        d_list[item] = counter + 1

    for k, v in d_list.items():
        print(f"{v} {k}")





def list():#fuction to get userinput and append to list

    my_list = []
    while True:
        try:
            my_list.append(input().upper())
        except KeyError:
            pass
        except EOFError:
            return my_list



main()
