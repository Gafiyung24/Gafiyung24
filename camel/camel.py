def main():
    x = input()

    snake_style()
#function to convert from camel style to snake style
def snake_style(user_input):
    for i in user_input:
        if user_input[i].isupper() is True:
            output = user_input[:i-1] + "_"
    return output
