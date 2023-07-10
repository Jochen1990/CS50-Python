amount_due = 50

while int(amount_due) > 0:
    print(f"Amount Due: {amount_due}")
    insert_coin = input("Insert Coin: ")
    if insert_coin not in ['25', '10', '5']:
        print(f"Amount due: {amount_due}")
    else:
        amount_due = amount_due - int(insert_coin)
        if amount_due <= 0:
            change_owed = amount_due * (-1)
            print(f"Change Owed: {change_owed}")

