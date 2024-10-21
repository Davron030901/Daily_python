'''n o‘lchamli a massiv berilgan(n-juft son). (indekslari o‘sish tartibida) Juft indeksdagi
elementlari chiqarilsin. a2,a4,…,an. Shart operatoridan foydalanilmasin.
6
1 2 3 4 5 6
2 4 6'''
n = int(input("element sonini kiriting:"))
a=[k for k in range(1,n+1)]
print([a[i] for i in range(1,len(a),2)])