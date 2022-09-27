import math
def distance(a, b):
    d = 0
    for i in range(2):
        d += pow((a[i] - b[i]), 2)
    return d
Identify = ['X', 'Y', 'Z', 'T']
arr = []
print("enter the coordinates:")
for i in range(4):
    b = []
    print("coordinates:", Identify[i])
    for j in range(2):
        b.append(int(input()))
    arr.append(b)
flag = True
for i in range(2):
    for j in range(i + 1, 4):
        dist = distance(arr[i], arr[j])
        if flag or max_dist < dist:
            m1 = i
            m2 = j
            max_dist = dist
            flag = False
print(f'maximum distance from each other: {Identify[m1]} и {Identify[m2]}')
print(f'value of this distance:  {max_dist ** 0.5:.3f}')
