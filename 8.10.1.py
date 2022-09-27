import random
N = int(input())
M = int(input())
B = [[random.randrange(10) for i in range(N)] for j in range(N)]
for i in range(N, M):
    if B[i][j] >= 0:
        print('Max element:', B)
