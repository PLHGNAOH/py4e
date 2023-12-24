import math
a=float(input("enter a: "))
b=float(input("enterb: "))
c=float(input("enterc: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("The equation with counltless solutions")
        else:
            print("The equation no solution")
    else:
        x = -c/b
        print("The equation has solution is: ",x)
else:
    denta = float(b*b -4*a*c)
    if denta > 0:
        x1=float(-b + math.sqrt(denta))/(2*a)
        x2=float(-b - math.sqrt(denta))/(2*a)
        print("The equation has two distinct solutions: ",x1,x2)
    elif denta == 0:
        x = -b/(2*a)
        print("The equation has two double solutions: ",x)
    else:
        print("The equation has no solution")