from random import shuffle, randint
n = int(input())
b = [[randint(10,99) for i in range(n)] for j in range(n)]
shuffle(b)
for i in b:
    print(i)
print()
 
a = sum(b, [])
max1 = max(a[::n+1])
max2 = max(a[n-1::n-1][:n])
if max1 > max2:
    i1 = j1 = a[::n+1].index(max1)
else:
    i1 = a[n-1::n-1][:n].index(max2)
    j1 = n - 1 - i1
b[n//2][n//2], b[i1][j1] = b[i1][j1], b[n//2][n//2]
 
for i in b:
    print(i)
