def main():
    x = input("camelCase: ")
    snake_case = snake_style(x)
    print(f"snake_case: {snake_case}")
#function to convert from camel style to snake style
def snake_style(user_input):
    for i in user_input:
        if user_input[i].isupper() is True:
            output = user_input[:i-1] + "_"
        else:
            output = user_input
    return output

main()
