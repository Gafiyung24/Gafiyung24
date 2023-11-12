def main():
    x = input("camelCase: ")
    print(f"snake_case: {snake_style(x)}", end = "")
#function to convert from camel style to snake style
def snake_style(user_input):
    for i, u in enumerate(user_input):
        if u.isupper():
            output = user_input[:i-1] + "_"
        else:
            output = user_input
    return output

main()
