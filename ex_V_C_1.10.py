import math
n = int(input("enter n: "))
if n > 0:
    k = math.log10(n) / math.log10(2)
    if k == int(k):
        print(f"{n} la so co dang 2^k và k = {int(k)}")
    else:
        print(f"{n} khong phai la so co dang 2^k")
else:
    print("n khong hop le")
        