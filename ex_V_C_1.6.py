a = float(input("enter a: "))
b = float(input("enter b: "))
c = float(input("enter c: "))
d = float(input("enter d: "))
e = float(input("enter e: "))
f = float(input("enter f: "))

if a == d and b == e and c == f:
    print("The system of equations has infinitely many solutions")
elif a == d and b == e and c != f:
    print("the system of equations has no solutions!")
    
elif (e*a)-(d*b) != 0:
    y = (f*a - d*c) / ((e*a)-(d*b))
    if  a != 0:
        x = ((c - b*y) / a)
        print("x = ",x)
        print("y = ",y)   
    else:
        print("Invalid!! ")
else:
    print("Invalid")
