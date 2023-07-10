items = {}

while True:
    try:
        item = input()
        item = item.upper()
        qty = 1
        if item in items:
            items[item] = qty + 1
        else:
            items[item] = qty
    except EOFError:
        myKeys = list(items.keys())
        myKeys.sort()
        sorted_dict = {i: items[i] for i in myKeys}
        for keys in sorted_dict:
            print(sorted_dict[keys], keys)
        break