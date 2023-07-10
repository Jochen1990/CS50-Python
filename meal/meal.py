def main():
    user = input("What time is it? ")
    convert(user)
    if convert(user) >= 7 and convert(user) <= 8:
        print("breakfast time")
    elif convert(user) >= 12 and convert(user) <= 13:
        print("lunch time")
    elif convert(user) >= 18 and convert(user) <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    minutes = int(minutes) / 60
    clock = float(hours) + float(minutes)
    return clock

if __name__ == "__main__":
    main()