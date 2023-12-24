def minmax(data):
    minimum = data[0]
    maximum = data[0]
    for element in data[1:]:
        if element < minimum:
            minimum = element
        if element > maximum:
            maximum = element
    return (minimum, maximum)
print(minmax([5,4,3,2,1]))