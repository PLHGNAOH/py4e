a=float(input("enter a: "))
b=float(input("emter b: "))
if a == 0:
    if b == 0:
        print("the equation with coutless solutions")
    else:
        print("the equation has no solution")
else:
    x=float(-b/a)
    print("the equation has solution is: ",x)