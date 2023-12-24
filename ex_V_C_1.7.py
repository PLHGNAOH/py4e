import math
n= float(input("enter n: "))
number_of_digits = int(math.log10(n) + 1)
if  number_of_digits == 4:
    unit_row = n // 1000
    if unit_row == 1:
        print("mot ngan ",end=" ")
    elif unit_row==2:
        print("hai ngan ",end=" ")
    elif unit_row==3:
        print("ba ngan",end=" ")
    elif unit_row==4:
        print("bon ngan ",end=" ")
    elif unit_row==5:
        print("nam ngan ",end=" ")
    elif unit_row==6:
        print("sau ngan ",end=" ")
    elif unit_row==7:
        print("bay ngan ",end=" ")
    elif unit_row==8:
        print("tam ngan ",end=" ")
    elif unit_row==9:
        print("chin ngan ",end=" ")
    number_of_digits -=1
    n %= 1000 
if  number_of_digits == 3:
    unit_row = n // 100
    if unit_row == 1:
        print("mot tram ",end=" ")
    elif unit_row==2:
        print("hai tram ",end=" ")
    elif unit_row==3:
        print("ba tram ",end=" ")
    elif unit_row==4:
        print("bon tram ",end=" ")
    elif unit_row==5:
        print("nam tram ",end=" ")
    elif unit_row==6:
        print("sau tram ",end=" ")
    elif unit_row==7:
        print("bay tram ",end =" ")
    elif unit_row==8:
        print("tam tram ",end=" ")
    elif unit_row==9:
        print("chin tram ",end=" ")
    number_of_digits -= 1
    n%=100
if  number_of_digits == 2:
    unit_row = n // 10
    if unit_row == 1:
        print("muoi",end=" ")
    elif unit_row==2:
        print("hai muoi ",end=" ")
    elif unit_row==3:
        print("ba muoi ",end=" ")
    elif unit_row==4:
        print("bon muoi",end=" ")
    elif unit_row==5:
        print("nam muoi",end="")
    elif unit_row==6:
        print("sau muoi ",end=" ")
    elif unit_row==7:
        print("bay muoi ",end=" ")
    elif unit_row==8:
        print("tam muoi ",end=" ")
    elif unit_row==9:
        print("chin muoi ",end=" ")
    number_of_digits-=1
        
if  number_of_digits == 1:
    unit_row = n % 10
    if unit_row == 1:
        print("mot")
    elif unit_row==2:
        print("hai")
    elif unit_row==3:
        print("ba")
    elif unit_row==4:
        print("bon")
    elif unit_row==5:
        print("nam")
    elif unit_row==6:
        print("sau")
    elif unit_row==7:
        print("bay")
    elif unit_row==8:
        print("tam")
    elif unit_row==9:
        print("chin")