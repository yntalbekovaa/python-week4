n=int(input())
a=[]
for i in range(n):
   a.append(list(map(int, input().split())))
for i in range(n):
   for j in range(n):
       if j>i:
           a[i][j]=0
       elif a[i][j]>0:
           a[i][j]=1
       else:
           a[i][j]=0
for i in range(n):
   print(*a[i])

