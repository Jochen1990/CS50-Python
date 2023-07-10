x, y, z = input("Expression: ").strip().split(" ")

x = int(x)
z = int(z)
if y == "+":
    result = x + z
    print(float(result))
elif y == "-":
    result = x - z
    print(float(result))
elif y == "*":
    result = x * z
    print(float(result))
elif y == "/":
    result = x / z
    print(float(result))


