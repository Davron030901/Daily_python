'''n o‘lchamli a massiv berilgan. 2 ta yangi b va c massivlarni ifodalang. b massivga a
massivning barcha musbat elementlari, c massivga manfiy elementlari (keyingi elementlarning
kirgizilgan tartibini saqlagan holda) yozilib, avval b massivning o‘lchami va tarkibi, keyin c
massivning o‘lchami va tarkibi chiqarilsin.
5
-2 8 -4 3 7
3
8 3 7
2
-2 -4'''
import random
n=int(input('element sonini kiriting:'))
a=[random.randint(-10,n-4) for _ in range(n)]
b=[]
c=[]
print(a)
for i in range(len(a)):
    if a[i]>0:
        b.append(a[i])
    else:
        c.append(a[i])
print(len(b),'\n',b,'\n',len(c),'\n',c)