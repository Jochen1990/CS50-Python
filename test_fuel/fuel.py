def main():
    while True:
        tank = input("Fraction: ")
        try:
            if not "/" in tank:
                continue
            tank2 = tank.split("/")
            tank1 = int(tank2[0])
            tank2 = int(tank2[1])
            if tank1 > tank2:
                continue
            result = convert(tank)
            indicator = gauge(result)
            if indicator == 'E':
                print("E")
                break
            elif indicator == "F":
                print("F")
                break
            else:
                print(indicator)
                break
        except ZeroDivisionError:
            pass
        except ValueError:
            pass

def convert(fraction):
    tank = fraction
    tank2 = tank.split("/")
    try:
        tank1 = int(tank2[0])
    except ValueError:
        print("tank1 is not an int")
    try:
        tank2 = int(tank2[1])
    except ValueError:
        print("tank2 is not an int")
    if tank1 > tank2:
        raise ValueError("tank1 cannot be greater than tank2")
    elif tank2 == 0:
        raise ZeroDvisionError("zero division not allowed")
    result = tank1 / tank2
    result = float(result) * 100
    result = int(round(result))
    return round(result)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return (f"{percentage}%")

if __name__ == "__main__":
    main()

