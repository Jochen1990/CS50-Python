import csv
import sys

list_before = []

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

elif sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv") != True:
    sys.exit("please pick two csv files")

else:
    with open(sys.argv[1]) as before:
        reader = csv.DictReader(before)
        for row in reader:
            list_before.append({"first": row["name"].split(",")[1].lstrip(), "last": row["name"].split(",")[0], "house": row["house"]})
        keys = list_before[0].keys()
        with open(sys.argv[2], "w") as after:
            writer = csv.DictWriter(after, keys)
            writer.writeheader()
            writer.writerows(list_before)
