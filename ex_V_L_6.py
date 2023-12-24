n=int(input("enter n: "))
a1=0
a2=1
if n >=1:
    if n ==1:
        print(a1)
    elif n == 2:
        print(a1,a2)
    else:
        for i in range(n):
          a1, a2=a2, a1+a2
          print(a1)
else:
    print("nhap lai")


