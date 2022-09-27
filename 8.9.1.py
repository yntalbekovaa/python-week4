from random import randint
import math
size = int(input("Enter matrix size: "))
minimum = int(input("Enter the minimum value of the matrix: "))
maximum = int(input("Enter the maximum value of the matrix: "))
a = [[randint(minimum,maximum) for j in range(size)]
for i in range(size)]
for row in a:
print(*row)
