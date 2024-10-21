'''n(n≤15) o‘lchamli butun tipli a massiv berilgan. Massivdagi indeksi 3 ga karrali bo‘lgan (3, 6,
…) elementlar yangi butun tipli b massivga yozilib, hosil qilingan b massivning o‘lchami va
elementlari chiqarilsin. Shart operatoridan foydalanilmasin.
9
1 3 7 4 5 8 6 9 2
3
7 8 2'''
import random
n=int(input('element sonini kiriting:'))
a=[random.randint(1,n+5) for _ in range(n)]
b=[]
print(a)
for i in range(2,len(a),3):
    b.append(a[i])
print(len(b),b)