from pyfiglet import Figlet
import sys
import random

user_input = input("Input: ")
figlet = Figlet()
if len(sys.argv) == 1:
    f = figlet.getFonts()
    rf = random.choice(f)
    figlet.setFont(font=rf)
    print(figlet.renderText(user_input))

elif "-f" or "--font" == sys.argv[1]:
    figlet.setFont(font = sys.argv[2])
    print(figlet.renderText(user_input))
elif "-f" or "--font" != sys.argv[1] and sys.argv[2] not in figlet.getFonts():
    sys.exit("Invalid")
