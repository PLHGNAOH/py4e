'''#enter an integer n, then reverse it
n=int(input("enter an integer n: "))
reverse_number=0
while  n>0:
    a= n%10
    reverse_number=reverse_number*10+a
    n=n//10
print(reverse_number)'''

def reverse_list(list):
    empty_list=[]
    index=len(list)-1
    while index >=0:
        empty_list.append(list[index])
        index -=1
    return empty_list
list=[1,2,3,4,5]
print(reverse_list(list))