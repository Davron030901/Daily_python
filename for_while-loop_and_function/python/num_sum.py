'''x haqiqiy va n butun (n>0) sonlari berilgan.
 
n
x x x
x
2 3 n 1 n
1
...
2 3


   
. Ifodaning qiymati
hisoblansin.
3.0 2 -1.5'''
x=float(input('Haqiqiy son kiriting:'))
n=int(input('Son kiriting:'))
mult=1
sum=0
for i in range(1,n+1 ):
    mult*=((-1)**(i+1))*x
    sum+=mult/i
print(sum)