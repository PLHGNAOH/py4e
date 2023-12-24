def is_multiple(m,n):
    if n % m == 0:
        print("n is a multiple of m")
        return True
    else:
        print("n is not a multiple of m")
        return False
n=int(input("enter a interger n: "))
m=int(input("enter a interger m: "))
print(is_multiple(m,n))