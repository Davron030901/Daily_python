'''r soni va n o‘lchamli a massiv berilgan. r soniga eng yaqin bo‘lgan massiv elementlari
topilsin.(shunday ak element bo‘lsa |ak-r| qiymat minimal bo‘ladi)'''
import random
r=float(input('haqiqiy son kiriting:'))
n=int(input('element sonini kiriting:'))
g=[random.randint(1,n) for _ in range(n)]
print(g)
count=max(g)
for i in g:
    if abs(g[i]-r)<count:
        count=g[i]
print(count)