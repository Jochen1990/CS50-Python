while True:
    tank = input("Fraction: ")
    try:
        tank2 = tank.split("/")
        tank1 = int(tank2[0])
        tank2 = int(tank2[1])
        result = tank1 / tank2
        result = float(result) * 100
        result = int(round(result))
        if not "/" in tank:
            pass
        elif tank1 > tank2:
            pass
        elif result <= 1:
            print("E")
            break
        elif result >= 99:
            print("F")
            break
        else:
            print(f"{round(result)}%")
            break
    except ZeroDivisionError:
        pass
    except ValueError:
        pass

