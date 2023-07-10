text = input("Input: ")
print("Output: ", end="")

for t in text:
    if t in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        t = ""
        print(t, end="")
    else:
        t = t
        print(t, end="")
print()
