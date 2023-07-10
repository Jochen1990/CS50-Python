import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        try:
            x, y = generate_integer(level)
            result = x + y
            answer_user = input(f"{x} + {y} = ")
            answer_user = int(answer_user)
            while answer_user == result:
                score += 1
                break
            counter = 0
            while answer_user != result:
                counter += 1
                if counter < 3:
                    print("EEE")
                    answer_user = input(f"{x} + {y} = ")
                    answer_user = int(answer_user)
                    pass
                else:
                    print(f"{x} + {y} = {result}")
                    break
        except ValueError:
            break
    print(score)


def get_level():
    level = input("Level: ")
    while level.isnumeric() == False:
        level = input("Level: ")
    level = int(level)
    while level < 1 or level > 3:
        level = input("Level: ")
        level = int(level)
    return level


def generate_integer(level):
    if level == 1:
        levelstart = 0
    else:
        levelstart = 10 ** (level - 1)
    levelend = (10**level) - 1
    x = random.randint(levelstart, levelend)
    y = random.randint(levelstart, levelend)
    return x, y


if __name__ == "__main__":
    main()
