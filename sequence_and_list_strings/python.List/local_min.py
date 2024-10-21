'''n o‘lchamli massiv berilgan. Uning birinchi lokal minimumining indeksi topilsin. (lokal
minimum – o‘zining har ikki yonidagi elementdan kichik bo‘lgan element)'''
import random
n=int(input('element sonini kiriting:'))
g=[random.randint(1,n) for _ in range(n)]
print(g)
for i in range(1,len(g)):
    if g[i-1]>g[i] and g[i+1]>g[i]:
        count=i
        break
print(count)