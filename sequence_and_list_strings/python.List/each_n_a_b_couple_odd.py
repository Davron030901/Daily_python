'''n o‘lchamli butun tipli a massiv berilgan. Shunday o‘lchamli yangi butun tipli b massivga a
massivning avval barcha juft indeksdagi elementlari keyin toq indeksdagi elementlari yozilsin.
a2,a4,…a1,a3,… Shart operatoridan foydalanilmasin.
6
2 4 8 7 3 9 4 7 9 2 8 3'''
import random
n=int(input('element sonini kiriting:'))
a=[random.randint(1,n+5) for _ in range(n)]
b=[]
print(a)
for i in range(1,len(a),2):
    b.append(a[i])
for i in range(0,len(a),2):
    b.append(a[i])
print(b)