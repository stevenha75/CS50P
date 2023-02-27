import sys
from pyfiglet import Figlet
import random

if len(sys.argv) == 3 or len(sys.argv) == 1:
    # Creating figlet object
    figlet = Figlet()

    # Checking preconditions
    if len(sys.argv) == 3:
        if not (
            ((sys.argv[1] == "-f") or (sys.argv[1] == "--font"))
            and (sys.argv[2] in figlet.getFonts())
        ):
            sys.exit("Invalid Arguments")

    # If no arguments select font randomly
    # use random library https://docs.python.org/3/library/random.html
    if len(sys.argv) == 1:
        f = random.choice(figlet.getFonts())
        figlet.setFont(font=f)

    # if two arguments select font based off of the second argument
    if len(sys.argv) == 3:
        f = sys.argv[2]
        figlet.setFont(font=f)

    s = input("Input: ")
    print("Output:\n" + figlet.renderText(s))
else:
    sys.exit("Invalid Argument Count")
