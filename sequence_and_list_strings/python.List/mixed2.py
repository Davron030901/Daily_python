'''n o‘lchamli a massiv berilgan. Uning elementlari quyidagi tartibda chiqarilsin: a1, a2, an, an-1,
a3, a4, an-2, an-3, ……(n-juft son).
6
1 3 4 5 2 8 1 3 8 2 4 5'''
import random
n=int(input('element sonini kiriting:'))
a=[random.randint(1,n+5) for _ in range(n)]
b=[]
print(a)
i=0
j=1
k=0
while i!=len(a)/4:
    if i%1==0.25 or i%1==0.0:
        b.append(a[k])
        k+=1
    else:
        b.append(a[len(a)-j])
        j+=1
    i+=0.25
print(len(b),b)