matrix = [[]] 
d= []
for i in range(len(matrix)):
d.append(matrix[i][i])
print(d)
print(sum(d))
summary = 0
for i in d:
summary += i
print(summary)
for i in range(len(matrix)):
if i+1 % 2 == 0:
for j in range(len(matrix[i])):
matrix[i][j]  /= summary
print(matrix)
