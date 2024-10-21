'''. n o‘lchamli butun sonli a massiv berilgan. Massivdagi barcha juft sonlar yangi butun tipli b
massivga yozilsin(shu tartibda) va hosil qilingan b massivning o‘lchami hamda uning elementlari
chiqarilsin.
5
8 5 9 6 1 2 8 6'''
import random
n=int(input('element sonini kiriting:'))
a=[random.randint(1,n+5) for _ in range(n)]
b=[]
print(a)
for i in range(len(a)):
    if a[i]%2==0:
        b.append(a[i])
print(len(b),b)