a = int(input("enter a: "))
b = int(input("enter b: "))

while b!=0:
    a,b=b, a % b
print(a)