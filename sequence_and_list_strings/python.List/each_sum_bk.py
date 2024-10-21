'''n o‘lchamli a massiv berilgan. Quyidagi tartib bo‘yicha shunday o‘lchamli yangi b massiv
ifodalansin. bk elementi a massivning 1-dan k gacha indeksli elementlar yig‘indisiga teng.(k ham
kiradi.)
6
2 4 8 7 3 9 2 6 14 21 24 33'''
import random
n=int(input('element sonini kiriting:'))
a=[random.randint(1,n+5) for _ in range(n)]
b=[]
print(a)
for i in range(1,len(a)+1):
    b.append(sum(a[:i]))
print(b)