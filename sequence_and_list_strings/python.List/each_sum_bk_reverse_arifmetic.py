'''n o‘lchamli a massiv berilgan. Shunday o‘lchamli yangi b massiv quyidagi tartib(qoida)
bo‘yicha ifodalansin: bk elementi a massivning k-dan n-gacha indeksli elementlari o‘rta
arifmetigiga teng. (n ham kiradi.)
6
2 4 6 8 10 12 7 8 9 10 11 12'''
import random
n=int(input('element sonini kiriting:'))
a=[random.randint(1,n+5) for _ in range(n)]
b=[]
print(a)
for i in range(len(a)):
    sum=0
    for j in range(i,len(a)):
        sum+=a[j]
    b.append(sum/(len(a)-i))
print(b)