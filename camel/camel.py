def main():
    camel_case = input("camelCase: ")
    print("snakeCase: ", end="")
    for c in camel_case:
        d = swap(c)
        print(f"{d}", end="")
    print()

def swap(letter):
    if letter.isupper() == True:
        letter = "_" + letter.lower()
        return letter
    else:
        return letter

main()
