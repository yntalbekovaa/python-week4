import random
matrix = [[random.randint(-10, 10) for _ in range(3)] for _ in range(3)]
print('Source Matrix:',matrix)
s=[]
for i in range(len(matrix)):
    s.append(sum(matrix[i]))
print("Row with the highest amount:",matrix[s.index(max(s))],"Sum of elements:",max(s),"The row with the smallest sum:",matrix[s.index(min(s))],"Sum of elements:",min(s))
