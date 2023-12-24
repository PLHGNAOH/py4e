a = float(input("enter a: "))
b = float(input("enter b: "))
c = float(input("enter c: "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Invalid triangle!!")
else: 
    if a == b and b == c:
        print("equilateral triangle!!")
    elif a == b or a == c or b == c:
        if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
            print("isosceles right triangle")
        print("isosceles triangle")
    elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        print("Right Triangle ")
    else:
        print("regular triangle")
    
        
        
        