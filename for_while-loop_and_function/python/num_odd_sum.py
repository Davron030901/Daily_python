'''x haqiqiy (|x|<1) va n butun (n>0) sonlari berilgan.
 
2 1
1
...
3 5
3 5 1 2 1


   
 
n
x x x
x
n n
.
Ifodaning qiymati hisoblansin.
0.5 2 0.46'''
x=float(input('Haqiqiy son kiriting:'))
n=int(input('Son kiriting:'))
mult=x
sum=0
for i in range(1,n+1 ):
    sum+=mult/(2*i-1)
    mult*=(-1)*(x**2)
print(sum)