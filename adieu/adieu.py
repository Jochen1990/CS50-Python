import inflect

names = []

while True:
    try:
        input_user = input("Name: ")
        names.append(input_user)
    except EOFError:
        print()
        if len(names) == 2:
            print("Adieu, adieu, to ", end = "")
            for i in range(len(names) - 1):
                print(names[i], end=" ")
            print("and", names[-1])
        elif len(names) == 1:
            print("Adieu, adieu, to", names[0])
        else:
            print("Adieu, adieu, to ", end = "")
            for i in range(len(names) - 1):
                print(names[i], end=", ")
            print("and", names[-1])
        break