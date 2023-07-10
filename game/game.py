import random

level = input("Level: ")
while level.isnumeric() == False:
    level = input("Level: ")
level = int(level)
while level < 1:
    level = input("Level: ")
level = int(level)
randomnr = random.randint(1, level)

print(randomnr)

while True:
    try:
        input_user = input("Guess: ")
        input_user = int(input_user)
        while input_user < 1:
            input_user = input("Guess: ")
            input_user = int(input_user)
        if input_user == randomnr:
            print("Just right!")
            break
        elif input_user < randomnr:
            print("Too small!")
        else:
            print("Too large!")
    except ValueError:
        pass