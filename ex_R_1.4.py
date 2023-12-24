def sum_of_squares(n):
    sum = 0
    for i in range(1,n):
        sum += i**2
    return sum
n=int(input("enter an integer n: "))
print(sum_of_squares(n))