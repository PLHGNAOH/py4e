def is_even(k):
    # Perform a bitwise AND with 1 and check if the result is 0
    if (k & 1) == 0:
        print("k i an even interger!")
        return True
    else:
        print("k is not an odd interger!")
        return False
k=int(input("enter an interger k: "))
print(is_even(k))   