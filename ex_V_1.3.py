n=int(input("enter TNCT: "))
LCB=650000
if n < 12:
    hs=1.92
elif n>=12 & n<16:
    hs=2.34
elif n>=36 & n<60:
    hs=3
elif n>=60:
    hs=4.5
l=hs*LCB
print("Your salary is: ",l)
    
