from random import randint
size = int(input("Enter the size of the matrix: "))
minimum = int(input(" Enter the minimum value of the matrix:"))
maximum = int(input("Enter the maximum value of the matrix: "))
a = [[randint(minimum,maximum) for j in range(size)] 
    for i in range(size)]
for row in a:
    print(*row)
amax = a[0][0]
imax = jmax = 0
for i in range(size):
    for j in range(size):
        if amax < a[i][j]:
            imax, jmax = i, j 
            amax = a[i][j]
print(amax)
a = [[a[i][j] for j in range(size) if j != jmax] 
    for i in range(size) if i != imax]
for row in a:
    print(*row)
