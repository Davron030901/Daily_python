'''n (n>1) butun son berilgan. Haqiqiy tipli ak ketma-ketlik quyidagicha aniqlanadi.
a1=1; a2=2; 2
2
2 1
 

k k
k
a a
a
, k=3,4,…. a1,a2, …, an elementlari chiqarilsin'''
n=int(input('Butun son kiriting: '))
a1=1
a2=2
print(a1,end=' ')
for i in range(3,n+1):
    a1=(a1+2*a2)/2
    print(a2,a1,end=' ')
    a2=(a2+2*a1)/2