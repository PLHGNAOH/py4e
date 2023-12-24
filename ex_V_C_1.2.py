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
        t = -c/b
        if t < 0:
            print("The equation no solution")  
        else:
            x1=math.sqrt(t)
            x2=-x1
            print("The equation has two solution: ",x1,x2) 
else:
    denta = float(b*b -4*a*c)
    if denta > 0:
        t1=float(-b + math.sqrt(denta))/(2*a)
        t2=float(-b - math.sqrt(denta))/(2*a)
        if t1 and t2 < 0:
             print("The equation no solution")
        if t1 >= 0:
            x1=math.sqrt(t1)
            x2=-x1
            print("The equation has two solution: ",x1,x2)
        if t2 >= 0:
            x1=math.sqrt(t2)
            x2=-x1
            print("The equation has two solution: ",x1,x2)       
    elif denta == 0:
        t = -b/(2*a)
        if t < 0:
            print("The equation no solution")  
        else:
            x1=math.sqrt(t)
            x2=-x1
            print("The equation has two solution: ",x1,x2)
    else:
        print("The equation has no solution")