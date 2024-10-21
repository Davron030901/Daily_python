'''n o‘lchamli a massiv berilgan. Xuddi shunday o‘lchamli elementlari quyidagi ko‘rinishda
aniqlanadigan yangi b massiv hosil qilinsin.
bk=2ak agar ak<5,
aks holda bk= 2
k
a
.
5
3 5 9 6 1 6 2.5 4.5 3 2'''
import random
n=int(input('element sonini kiriting:'))
a=[random.randint(1,n+5) for _ in range(n)]
b=[]
for i in range(len(a)):
    if a[i]>=5:
        b.append(a[i]/2)
    else:
        b.append[a[i]*2]
print(b)