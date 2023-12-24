def sum_of_squares(n):
    sum = 0
    for i in range(1,n):
        if i % 2 != 0:
            sum += i**2
    return sum
n=int(input("enter a positive integer n: "))
print(sum_of_squares(n))