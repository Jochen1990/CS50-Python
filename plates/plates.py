def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0:2].isalpha():
        return False
    for i in range(len(s)):
        if (i - 1) > 0 and (i + 1) < len(s):
            if s[i].isdigit() and s[i + 1].isalpha():
                return False
            if not s[i].isalnum():
                return False
        elif s[i].isdigit() == True and s[i - 1] == '0':
                return False

    return True


main()