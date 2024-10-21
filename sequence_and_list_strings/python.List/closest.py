'''n o‘lchamli massiv berilgan. Massivning ikkita eng yaqin elementlari indekslari topilib(ya’ni
elementlar ayirmasi moduli eng kichkina bo‘lgan) o‘sish tartibida chiqarilsin. Bunday yig‘indilar
bir nechta bo‘lsa oxirgisi olinsin.'''
import random
n=int(input('element sonini kiriting:'))
g=[random.randint(1,n-2) for _ in range(n)]
print(g)
a=0
b=0
count=max(g)
print(count)
for j in range(len(g)):
    for i in range(j+1,len(g)):
        if abs(g[j]-g[i])<=count:
            count=abs(g[j]-g[i])
            a=j+1
            b=i+1
print(a,b)