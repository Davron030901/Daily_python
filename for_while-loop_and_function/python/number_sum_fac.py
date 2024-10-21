'''x haqiqiy va n butun sonlari berilgan(n≥0).
!
...
2!
1
2
n
x x
x
n
   
. Ifodaning qiymati
hisoblansin.
2 2 5'''
n=int(input('Son kiriting:'))
x=float(input('Haqiqiy son kiriting:'))
mult=1
sum=1
for i in range(1,n+1):
    mult*=(x)*(1/i)
    sum+=mult
print(sum)