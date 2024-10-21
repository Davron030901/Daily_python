'''n o‘lchamli a butun sonlar massivi berilgan. Berilgan o‘rin almashtirishlarda inversiyalar soni
topilsin. ( o’sish tartibida joylashtirilsin.)'''
import random
n=int(input('element sonini kiriting:'))
g=[random.randint(1,n-2) for _ in range(n)]
print(g)
a=0
for j in range(len(g)):
    for i in range(j+1,len(g)):
        if g[j]<g[i]:
            a+=1
print(a)