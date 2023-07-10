import sys
import csv

count = 0

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif sys.argv[1].endswith(".py") == False:
    sys.exit("Not a python file")

else:
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                line = line.strip()
                if line.startswith("#"):
                    pass
                elif len(line) == 0:
                    pass
                else:
                    count += 1
            print(count)

    except FileNotFoundError:
        sys.exit("File does not exist")





