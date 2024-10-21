''' n o‘lchamli massiv berilgan. Massivdagi yig‘indisi eng katta bo‘ladigan 2 ta yonma-yon
turuvchi elementlar topilib, bu elementlarning indekslari o‘sish tartibida chiqatirilsin. Bunday
yig‘indilar bir nechta bo‘lsa oxirgisi olinsin.'''
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