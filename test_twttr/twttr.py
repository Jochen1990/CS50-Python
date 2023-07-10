def main():
    text = input("Input: ")
    output = shorten(text)
    print(f"Output: {output}", end="")
    print()


def shorten(word):
    word = word.replace("a", "")
    word = word.replace("e", "")
    word = word.replace("i", "")
    word = word.replace("o", "")
    word = word.replace("u", "")
    word = word.replace("A", "")
    word = word.replace("E", "")
    word = word.replace("I", "")
    word = word.replace("O", "")
    word = word.replace("U", "")
    return(word)

if __name__ == "__main__":
    main()




