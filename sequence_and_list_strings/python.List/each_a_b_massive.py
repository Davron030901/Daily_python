'''Bir xil n o‘lchamli a va b massiv berilgan. a va b massivlardagi mos elementlarning qiymatlari
almashtirilsin. Avval a massivning o‘zgargan elementlari keyin b massivning o‘zgargan
elementlari chiqarilsin.
5
3 5 9 6 1
2 5 7 4 9
2 7 4 9
3 9 6 1'''
import random
n=int(input('element sonini kiriting:'))
a=[random.randint(1,n+5) for _ in range(n)]
b=[random.randint(1,n+5) for _ in range(n)]
c=[]
d=[]
print(a,'\n',b)
for i in range(len(a)):
    if a[i]!=b[i]:
        c.append(a[i])
        d.append(b[i])
b=c
a=d
print(a,'\n',b)