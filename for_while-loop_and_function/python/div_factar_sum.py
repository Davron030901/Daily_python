''' xЄR va nЄZ sonlari berilgan.
(2 1)!
( 1)
...
3! 5!
3 5 2 1


   

n
x x x
x
n n
. Ifodaning qiymati hisoblansin.
3 2 -1,5'''
x=float(input('Haqiqiy son kiriting:'))
n=int(input('Son kiriting:'))
mult=x
sum=0
for i in range(1,n+1 ):
    sum+=mult
    mult*=(-1)*(x**2)*(1/((2*i)*(2*i+1)))
print(sum)