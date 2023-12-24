n = int(input("enter n: "))
S=1
result=0
for i in range(1,n+1):
    S*=i
    result+=S
print("result: ",result)
    