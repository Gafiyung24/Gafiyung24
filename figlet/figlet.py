from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fig_f = "-f"
fig_font = "--font"

if len(sys.argv) == 1:
    user_input = input("Input: ")
    f = figlet.getFonts()
    rf = random.choice(f)
    figlet.setFont(font=rf)
    print(figlet.renderText(user_input))

elif len(sys.argv) == 3:
    if sys.argv[1] in [fig_f, fig_font] and sys.argv[2] in figlet.getFonts():
        user_input = input("Input: ")
        figlet.setFont(font = sys.argv[2])
        print(figlet.renderText(user_input))
    else:
        sys.exit()
elif len(sys.argv) == 2:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")
