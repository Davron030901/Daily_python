'''a haqiqiy va n butun sonlari berilgan(n>0).
a a a ... a.
n
   
(a, n marta ko‘paytirilgan) a ning
n- darajasi hisoblansin.
1,5 2 2,25'''
a=float(input('Son kiriting:'))
n=int(input('Darajani kiriting:'))
mult=1
for i in range(n):
    mult*=a
print(mult)