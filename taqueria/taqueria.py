tacos = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
pricelist =[]

while True:
    try:
        while True:
            order = input("Item: ").title()
            price = tacos[f"{order}"]
            pricelist.append(price)
            print(f'Total: ${sum(pricelist):.2f}')
    except KeyError:
        pass
    except EOFError:
        break


