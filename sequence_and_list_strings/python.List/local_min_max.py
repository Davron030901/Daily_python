'''n o‘lchamli massiv berilgan. Uning lokal minimumlari orasidan eng kattasi topilsin. (Agar
bunday element bo‘lmasa 0 chiqarilsin.)'''
import random
n=int(input('element sonini kiriting:'))
g=[random.randint(1,n) for _ in range(n)]
print(g)
count=0
for i in range(1,len(g)):
    if len(g)-1==i:
        break
    if g[i-1]>g[i] and g[i+1]>g[i]:
        if count<g[i]:
            count=g[i]
print(count)