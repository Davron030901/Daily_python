'''n o‘lchamli massiv berilgan. Uning oxirgi lokal maksimumining indeksi topilsin. (lokal
maksimum – o‘zining har ikki yonidagi elementdan katta bo‘lgan element)'''
import random
n=int(input('element sonini kiriting:'))
g=[random.randint(1,n) for _ in range(n)]
print(g)
for i in range(1,len(g)):
    if len(g)-1==i:
        break
    if g[i-1]<g[i] and g[i+1]<g[i]:
        count=i
    
print(count)