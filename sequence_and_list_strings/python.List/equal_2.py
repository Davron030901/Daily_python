'''Kamida ikkita bir xil elementga ega bo‘lgan n o‘lchamli butun tipli massiv berilgan. Bir xil
elementlarning indekslari aniqlanib, o‘sish tartibida chiqarilsin.'''
import random
n=int(input('element sonini kiriting:'))
g=[random.randint(1,n-2) for _ in range(n)]
print(g)
a=[]
for j in range(len(g)):
    for i in range(j+1,len(g)):
        if g[j]==g[i]:
            a.append(i)
    if len(a)!=0:
        a.insert(0,j)
        break
print(a)