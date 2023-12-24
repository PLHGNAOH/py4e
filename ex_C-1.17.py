# Get the input values for x, y, z and n
x = int(input())
y = int(input())
z = int(input())
n = int(input())

# Use list comprehension to generate a list of coordinates
coordinates = [(i, j, k) for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]

# Print the list of coordinates
print(coordinates)
