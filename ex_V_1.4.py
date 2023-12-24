n=int(input("enter an integer n: "))
c= n // 10
dv= n % 10
if n < 10 or n > 99:
    print("enter a number that has two digits!")
else:
    if c == 1:
        print("Muoi",end=" ")
    elif c == 2:
        print("Hai Muoi",end=" ")
    elif c == 3:
        print( "BA Muoi",end=" ")
    elif c == 4:
        print(" Bon Muoi",end=" ")
    elif c == 5:
        print("Nam Muoi",end=" ")
    elif c == 6:
        print("Sau Muoi",end=" ")
    elif c == 7:
        print("Bay Muoi",end=" ")
    elif c == 8:
        print("Tam Muoi",end=" ")
    elif c == 9:
        print("Chin Muoi",end=" ")


    if dv == 1:
        print("mot")
    elif dv==2:
        print("hai")
    elif dv==3:
        print("ba")
    elif dv==4:
        print("bon")
    elif dv==5:
        print("nam")
    elif dv==6:
        print("sau")
    elif dv==7:
        print("bay")
    elif dv==8:
        print("tam")
    elif dv==9:
        print("chin")
