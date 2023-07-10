import sys
import csv
from tabulate import tabulate

menu = []

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif sys.argv[1].endswith(".csv") != True:
    sys.exit("Not a .csv file")

else:
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        for row in reader:
            menu.append(row)
        print(tabulate(menu, headers="firstrow", tablefmt="grid"))
