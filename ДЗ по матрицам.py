from random import random
M = 5
N = 5
a = []
for i in range(N):
    b = []
    for j in range(M):
        b.append(round(random()*8))
    a.append(b)
    print(b)
print()
for i in range(N):
    a[i][i]=0
    print(a[i])

    
