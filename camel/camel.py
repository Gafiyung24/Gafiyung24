def main():
    x = input("camelCase: ")
    print(f"snake_case: {snake_style(x)}", end = "")
#function to convert from camel style to snake style
def snake_style(user_input):
    output = ""
    for i in user_input:
        if i.isupper():
            output = output + "_"
        else:
            output = user_input
    return output

main()
