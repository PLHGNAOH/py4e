import math
n =int(input("enter n: "))
soluongchuso=int(math.log10(n)+1)
print("So luong chu so: ",soluongchuso)
Min=n%10
Max=n%10
n//=10
while n > 0:
    ss= n%10
    if ss < Min:
        Min=ss
    elif ss > Max:
        Max=ss
    n//=10   
print("Min: ",Min)
print("Max: ",Max)