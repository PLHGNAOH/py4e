def odd_product(sequence):
    for i in range(len (sequence)):
        for j in range(len(sequence)):
            if i != j :
                product= sequence[i] * sequence[j]
                if product % 2 == 1:
                    return True
    return False
print(odd_product([1,2,4,7]))