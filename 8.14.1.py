from random import randint
 
m = 3
l = [[randint(-10, 10) for j in range(5)] for i in range(5)]
print(*l, sep='\n')
print()
 
ll = []
for i in range(len(l)):
    ll.append(l[i][i])
 
maxid = ll.index(max(ll))
l[maxid], l[m] = l[m], l[maxid]
print(*l, sep='\n')
