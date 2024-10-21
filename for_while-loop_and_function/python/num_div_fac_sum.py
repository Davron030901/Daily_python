'''x haqiqiy va n butun (n≥0) sonlari berilgan.
2 !
( 1)
...
2! 4!
1
2 4 2
n
x x x
n n

   
. Ifodaning qiymati
hisoblansin.
2.0 1 -1'''
x=float(input('Haqiqiy son kiriting:'))
n=int(input('Son kiriting:'))
mult=1
sum=1
for i in range(1,n+1 ):
    mult*=(-1)*(x**2)*(1/((2*i-1)*(2*i)))
    sum+=mult
print(sum)