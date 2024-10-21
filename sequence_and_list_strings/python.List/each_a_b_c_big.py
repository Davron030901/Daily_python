'''Bir xil n o‘lchamli 2 ta a va b massivlar berilgan. Shunday c massiv tuzilsin: c massivning iindeksdagi elementi a va b massivlarning i-indeksdagi elementlarining kattasidan iborat bo‘lsin.
5
3 5 9 6 1
2 5 7 4 9
3 5 9 6 9'''
import random
n=int(input('element sonini kiriting:'))
a=[random.randint(1,n+5) for _ in range(n)]
b=[random.randint(1,n+5) for _ in range(n)]
c=[]
print(a,'\n',b)
for i in range(len(a)):
    if a[i]>b[i]:
        c.append(a[i])
    else:
        c.append(b[i])
print(c)