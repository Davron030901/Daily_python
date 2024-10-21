'''n(n≤15) o‘lchamli butun tipli a massiv berilgan. a massivning toq indeksdagi barcha
elementlarini yangi butun tipli b massivga yozib, hosil qilingan b massivning o‘lchami hamda
uning elementlari chiqarilsin. Shart operatoridan foydalanilmasin.
5
8 5 9 6 1
3
8 9 1'''
import random
n=int(input('element sonini kiriting:'))
a=[random.randint(1,n+5) for _ in range(n)]
b=[]
print(a)
for i in range(0,len(a),2):
        b.append(a[i])
print(len(b),b)