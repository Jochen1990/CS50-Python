def convert():
    output = input().replace(":)", "🙂").replace(":(", "🙁")
    return output

def main():
    print(convert())

main()