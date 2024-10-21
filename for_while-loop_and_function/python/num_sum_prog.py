'''x haqiqiy (|x|<1) va n butun (n>0) sonlari berilgan.
 
2 4 ... 2 (2 1)
1 3 .. 2 1
...
2 4 5
1 3
2 3
1
3 5 2 1
    
  
 
 






n n
x x n x
x
n
. Ifodaning qiymati hisoblansin'''
x=float(input('Haqiqiy son kiriting:'))
n=int(input('Son kiriting:'))
mult=x
sum=x
for i in range(1,n):
    mult*=(x**2)*((2*i-1)/2*i)
    sum+=mult/(2*i+1)
print(sum)