'''n(n>0) butun son berilgan.
n!12
...
n
(n-faktorial) ko‘paytma hisoblansin. Ifodaning
natijasi butun sonlar diapazonidan chiqib ketishi mumkinligi hisobga olinib, natijani saqlash uchun
haqiqiy tipli o‘zgaruvchidan foydalanilsin va natija ham haqiqiy son ko`rinishida chiqarilsin.
5 120'''
n=int(input('Son kiriting:'))
mult=1
for i in range(1,n+1):
    mult*=i
print(mult)