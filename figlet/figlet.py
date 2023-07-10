import pyfiglet
import sys
import random

fonts = (pyfiglet.FigletFont.getFonts())

if len(sys.argv) == 1:
    text = input("Input: ")
    result = pyfiglet.figlet_format(text, font = random.choice(fonts))
    print(result)

elif sys.argv[1] == '-f' or sys.argv[1] == '--font' and sys.argv[2] in fonts:
    text = input("Input: ")
    font1 = sys.argv[2]
    result = pyfiglet.figlet_format(text, font = font1)
    print(result)

else:
    sys.exit("Invalid usage")

