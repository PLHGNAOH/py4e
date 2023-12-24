n=int(input("enter n: "))
checkTang=True
checkgiam=True
while n > 9:
    chuso1 = n % 10
    n //=10
    chuso2 = n % 10
    if chuso1 <= chuso2:
        checkTang = False
    elif chuso1 >= chuso2:
        checkgiam = False
         
if checkTang == True:
    print("tang dan")
elif checkgiam == True:
    print("giam dan")
else:
    print("khong tang khong giam")
    