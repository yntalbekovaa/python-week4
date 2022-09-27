import random 
n = int(input())
k = int(input())
arr = [[int(input()) for j in range(n)] for i in range(n)]
for i in range(n):
   for j in range(n):
       if k == i:
           arr[i][j] = arr[i][j] / arr[i][i]
print('n'.join([''.join([str(f'{i:4}') for i in row]) for row in arr]))


