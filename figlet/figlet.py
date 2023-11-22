from pyfiglet import Figlet
import sys
import random


figlet = Figlet()
if len(sys.argv) == 1:
    user_input = input("Input: ")
    f = figlet.getFonts()
    rf = random.choice(f)
    figlet.setFont(font=rf)
    print(figlet.renderText(user_input))

elif "-f" or "--font" == sys.argv[1]:
    user_input = input("Input: ")
    figlet.setFont(font = sys.argv[2])
    print(figlet.renderText(user_input))
elif "-f" or "--font" != sys.argv[1] or sys.argv[2] not in figlet.getFonts():
    sys.exit("Invalid usage")
elif 1 < len(sys.argv) < 3:
    sys.exit("Invalid usage")
