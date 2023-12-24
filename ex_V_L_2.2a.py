import math
n = int(input("enter: "))
tempt=n
soluongchuso=int(math.log10(n))
sodaonguoc=0
while tempt>0:
    tachso=tempt%10
    sodaonguoc+=tachso*math.pow(10,soluongchuso)
    tempt//=10
    soluongchuso-=1
if int(sodaonguoc) == n:
    print("la so do xung")
else:
    print("khong phai la so doi xung ")
    