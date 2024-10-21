'''r soni va n o‘lchamli massiv berilgan. Yig‘indisi r soniga eng yaqin bo‘lgan 2 ta yonma-yon
massiv elementlari topilib, bu elementlarning indekslari o‘sish tartibida chiqatirilsin. Bunday
yig‘indilar bir nechta bo‘lsa oxirgisi olinsin.'''
import random
r=float(input('haqiqiy son kiriting:'))
n=int(input('element sonini kiriting:'))
g=[random.randint(1,n) for _ in range(n)]
print(g)
j=0
k=0
count=max(g)
for i in range(len(g)):
    if abs((g[i]+g[i-1])-r)<count:
        count=abs(g[i]+g[i-1]-r)
        k=i+1
        j=i
print(j,k)