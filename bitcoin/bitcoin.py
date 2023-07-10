import requests
import sys
import json

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
elif sys.argv[1].isalpha() == True:
    sys.exit("Command-line argument is not a number")
else:
    try:
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        #print(json.dumps(r.json(), indent=2))
        output = r.json()
        multiplier = float(sys.argv[1])
        print(multiplier)
        dollars = (output["bpi"]["USD"]["rate"])
        dollars = dollars.replace(",", "")
        dollars = dollars.replace(".", "")
        dollars = float(dollars) / 10000
        result = dollars * multiplier
        result = float(result)
        print(f"${result:,.4f}")


    except requests.RequestException:
        pass