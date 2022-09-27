import random
n = int(input())
a = random.array([list(map(int, input().split())) for _ in range(n)])
a = a.transpose() 
for row in a:
    for elem in row:
        print(elem, end=' ')
    print()
