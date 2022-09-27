from random import randint as rd 
m, n = map(int,input().split())
arr = [[rd(1, 10) for i in range(m)] for j in range(n)]
for i in arr :
    print(*i)
print()
for row in arr :
    rmin = min(row)
    row = [(1 if rmin % 2 else 0) if j == rmin else j for j in row]
    print(*row)
