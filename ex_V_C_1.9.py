import math
n =int(input("enter n: "))
if n >= 0:
    result = math.sqrt(n)
    if result == int(result):
        print(f"{n} is a square number")
    else:
        print(f"{n} is not a square number")
else:
    print("Invalid number")