''' n (n>0)butun son berilgan. Haqiqiy tipli ak ketma-ketlik quyidagicha aniqlanadi.
a0=1; k
a
a
k
k
1 1


, k=1,2,.. Ketma-ketlikning a1, a2, …,an elementlari chiqarilsin.
2 2 1.5'''
n=int(input('Butun son kiriting: '))
ak=1
for i in range(1,n+1):
    ak=(ak+1)/i
    print(ak,end=' ')