from random import randint
 
N, M = 3, 4
a = [[randint(-50, 50) for _ in range(M)] for _ in range(N)]
for i in a:
    print(*sorted(i))
