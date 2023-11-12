def main():
    x = input("camelCase: ")
    print(f"snake_case: {snake_style(x)}")
#function to convert from camel style to snake style
def snake_style(user_input):
    output = ""
    for i in user_input:
        if i.isupper():
            output += "_"+i.lower()
        else:
            output +=i
    return output

main()
