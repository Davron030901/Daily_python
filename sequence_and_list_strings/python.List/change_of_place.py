'''n o‘lchamli butun sonli massiv berilgan. Agar u o‘rin almashtirishlardan iborat bo‘lsa ya`ni 1
dan to n gacha hamma sonlarni o‘z ichiga olsa 0 chiqarilsin aks holda 1-qonuniyatni buzadigan
element indeksi chiqarilsin. '''
import random
n=int(input('element sonini kiriting:'))
g=[random.randint(1,n-2) for _ in range(n)]
print(g)
a=0
for j in range(len(g)):
    if (g[j]-g[j-1])!=(g[-1]-g[-2]):
            a=j+2
            break
print(a)