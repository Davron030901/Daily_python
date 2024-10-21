'''n (n>0) butun son berilgan. Haqiqiy tipli ak ketma-ketlik quyidagicha aniqlanadi.
a0=2;
1
1
2

 
k
k
a
a
k=1,2,…Ketma-ketlikning a1,a2, …, an elementlari chiqarilsin.
2 2.5 2.4'''
n=int(input('Butun son kiriting: '))
ak=2
for i in range(n):
    ak=2+1/ak
    print(ak,end=' ')
