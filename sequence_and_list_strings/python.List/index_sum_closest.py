''' r soni va n o‘lchamli massiv berilgan. Yig‘idisi r ga eng yaqin bo‘lgan 2 ta element topilib,
indekslari berilgan tartibda chiqarilsin. Bunday yig‘indilar bir nechta bo‘lsa oxirgisi olinsin.'''
import random
r=float(input('haqiqiy son kiriting:'))
n=int(input('element sonini kiriting:'))
g=[random.randint(1,n-2) for _ in range(n)]
print(g)
a=0
b=0
count=max(g)
print(count)
for j in range(len(g)):
    for i in range(j+1,len(g)):
        if abs(g[j]+g[i]-r)<=count:
            count=abs(g[j]+g[i]-r)
            a=j+1
            b=i+1
print(a,b)