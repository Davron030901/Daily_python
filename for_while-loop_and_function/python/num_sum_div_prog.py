''' x haqiqiy (|x|<1) va n butun (n>0) sonlari berilgan.
 
 
n
x x x n x
n
n
2 4 2
2 3
... 1 1 3 ...
2 4 6
1 3
2 2 4
1
3 3 1
 

      
 



 

. Ifodaning qiymati hisoblansin.
0.5 2 1.25'''
x=float(input('Haqiqiy son kiriting:'))
n=int(input('Son kiriting:'))
mult=1
sum=1
for i in range(1,n):
    mult*=(-1)*((2*i-3)/2*i)
    sum+=mult*(x**(i*2-1))
print(sum)