import random
 
N = int(input())
M = int(input())
B = [[random.randrange(10) for i in range(M)] for j in range(N)]
 
for i in B:
    print(*map('{:3}'.format, i))
 
for i in range(0, len(B)):
    if (i % 2) == 1:
        for j in range(0, len(B[i])):
            k = 11
            if k > B[i][j]:
                k = B[i][j]
        print(k)
