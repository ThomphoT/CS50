import random
import sys

from pyfiglet import Figlet


def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        figlet.setFont(font=random.choice(fonts))
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
        if sys.argv[2] not in fonts:
            sys.exit("Invalid usage")
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Invalid usage")

    text = input("Input: ")
    print(figlet.renderText(text), end="")


main()
