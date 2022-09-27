from random import randint
n = 5 
a = [[randint(-99, 99) for j in range(n)] for i in range(n)]
for row in a:
    print(*map('{:>3d}'.format, row))
imax = jmax = 0
rmax = []
cmin = a[0].copy()
amax = a[0][0]
for i in range(n):
    if a[i][i] > amax:
        imax = i
        jmax = i 
        amax = a[i][i]
    if a[i][n-i-1] > amax:
        imax = i 
        jmax = n-i-1
        amax = a[i][n-i-1]
    tmax = a[i][0]
    for j in range(n):
        if tmax < a[i][j] :
            tmax = a[i][j]
        if cmin[j] > a[i][j]:
            cmin[j] = a[i][j]
    rmax.append(tmax)            
        
a[n//2][n//2], a[imax][jmax] = a[imax][jmax], a[n//2][n//2]
print('row maxima:')
print(*rmax)
print('column minima:')
print(*cmin)
print()
for row in a:
    print(*map('{:>3d}'.format, row))
import numpy as np
n = 5
a = np.random.randint(-99, 99, (n, n))
print(a)
 
ij = np.divmod(np.argmax(np.hstack
     ((np.diag(a), np.diag(np.rot90(a))))), n)
i = ij[1]
j = (n - 2*i - 1) * ij[0] + i
 
print('row maxima:')
print(a.max(axis=0))
print('column minima:')
print(a.min(axis=1))
a[i,j], a[n//2,n//2] = a[n//2,n//2], a[i,j]
print()
print(a)
