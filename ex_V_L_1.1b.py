import math
n = int(input("enter n: "))
sum=0
for i in range(1,n+1):
    sum+=int(math.pow(i,2))
print("sum: ",sum)