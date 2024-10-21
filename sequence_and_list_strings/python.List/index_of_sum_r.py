import random
n=int(input('element sonini kiriting:'))
g=[random.randint(1,n) for _ in range(n)]
print(g)
j=0
k=0
count=min(g)
for i in range(len(g)):
    if g[i]+g[i-1]>count:
        count=g[i]+g[i-1]
        k=i+1
        j=i
print(j,k)