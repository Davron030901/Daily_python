'''n o‘lchamli a massiv berilgan. Uning elementlari quyidagi tartibda chiqarilsin: a1, an, a2, an-1,
a3, an-2, ...
6
1 3 4 5 2 8 -------1 8 3 2 4 5'''
import random
n=int(input('element sonini kiriting:'))
a=[random.randint(1,n+5) for _ in range(n)]
b=[]
print(a)
i=0
while i!=len(a)/2:
    if i%1==0:
        b.append(a[int(i)])
    else:
        b.append(a[int(len(a)-i)])
    i+=0.5
print(len(b),b)