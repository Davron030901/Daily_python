'''. n o‘lchamli a massiv berilgan(n-toq son). Massivning toq indeksida turgan elementlari
indekslarini kamayish tartibida tartiblab chiqarilsin. an, an-2, an-4, … a1 shart operatoridan
foydalanilmasin.'''
n = int(input("element sonini kiriting:"))
a=[k for k in range(1,n+1)]
a=[a[i] for i in range(0,len(a),2)]
a.reverse()
print(a)