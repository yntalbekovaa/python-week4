n = 3
mas = []
i = 0
j = 0
while i < n:
    b = []
    i += 1
    while j < n:
        j += 1
        if j >= i:
            print("Enter [", i, ",", j, "] element")
            b.append(int(input()))
        else:
            print(end=" ")
        mas.append(b)
i = 1
while i < n:
    i += 1
    j = 0
    while j < i:
        j += 1
        mas[i][j] = mas[j][i]
print("The resulting matrix: ")
while i < n:
    i += 1
    while j < i:
        j += 1
        print(mas[i][j], end=" ")
    print()
