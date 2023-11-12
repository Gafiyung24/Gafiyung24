def main():

    snake_style()
#function to convert from camel style to snake style
def snake_style(user_input):
    for i in user_input:
        if user_input[i].isupper() is True:
            output = user_input
