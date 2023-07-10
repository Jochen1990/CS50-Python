import re
import sys


def main():
    s = input("HTML: ")
    print(parse(s))

def parse(s):
    match = re.search(r"(https?://)(?:www.)?(youtube\.com/embed/.+?[a-zA-Z09])\"", s)
    if match:
        output1 = match.group(1) + match.group(2)
        output2 = re.sub(r"be\.com", ".be", output1)
        output3 = re.sub(r"/embed", "", output2)
        output4 = re.sub(r"https?", "https", output3)
        return output4
    else:
        return None

if __name__ == "__main__":
    main()