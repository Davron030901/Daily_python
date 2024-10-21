'''n o‘lchamli a massiv berilgan. Shunday o‘lchamli yangi b massiv quyidagi qoida bo‘yicha
ifodalansin: bk elementi a massivning k-dan n-gacha indeksli elementlari yig‘indisiga teng. ( n
ham kiradi.)
6
2 4 6 8 10 12 42 40 36 30 22 12'''
import random
n=int(input('element sonini kiriting:'))
a=[random.randint(1,n+5) for _ in range(n)]
b=[]
print(a)
for i in range(len(a)):
    sum=0
    for j in range(i,len(a)):
        sum+=a[j]
    b.append(sum)
print(b)