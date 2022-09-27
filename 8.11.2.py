from random import randint
n = 3 
m = 9
a = [[randint(-19, 19) for j in range(m)]
     for i in range(n)]
 
n = len(a)
m = len(a[0])
max_a = abs(a[0][0])
for row in a:
    for el in row:
        max_a = max(abs(el), max_a)
 
tmp = pow(max_a + 1, n)
 
c = [1] * m 
for i in range(n):
    print(*map('{:2d}'.format, a[i]))
    for j in range(m):
        if abs(a[i][j]) < 10 and abs(c[j]) < tmp:
            c[j] *= a[i][j]
        else:
            c[j] = tmp
print()
 
if min(c) < tmp:
    ind = c.index(min(c))
    print('min: ', ind+1)
    ind = m - 2 if ind == m -1 else ind
    for i in range(n):
        for j in range(m):
            a[i][ind], a[i][ind+1] = a[i][ind+1], a[i][ind]
        print(*map('{:2d}'.format, a[i]))
else:
    print('no')
