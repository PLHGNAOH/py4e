n = int(input("enter n: "))
count=0
if n == 2:
    print("la so nguyen to")
else:
    if n > 2:
        for i in range(1,n+1):
            if n % i== 0:
                count+=1
        if count > 2:
            print("khong phai la so nguyen to")
        else:
            print("la so nguyen to")
    else:
        if n == 1:
            print("khong la so nguyen to")
        else:
            print("nhap lai")

    
    
    