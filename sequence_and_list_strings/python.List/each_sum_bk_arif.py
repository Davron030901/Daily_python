'''n o‘lchamli a massiv berilgan. Quyidagi qoida bo‘yicha shunday o‘lchamli yangi b massiv
tuzilsin: bk elementi a massivning 1-dan k-gacha indeksli elementlarining o‘rta arifmetigiga teng.
(k ham kiradi.)
6
2 4 6 8 10 12 2 3 4 5 6'''
import random
n=int(input('element sonini kiriting:'))
a=[random.randint(1,n+5) for _ in range(n)]
b=[]
print(a)
for i in range(1,len(a)+1):
    b.append(sum(a[:i])/i)
print(b)