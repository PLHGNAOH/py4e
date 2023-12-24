s = input("Enter a letter character: ")
if s.isalpha() and len(s) == 1:
    if s.islower:
        s = s.upper
        print("The character after conversion is: ",s)
    else:
        s = s.lower
        print("The character after conversion is: ",s)
else:
    print("Ivalid character!!")