''' n (n>1) butun son berilgan. Butun tipli fk fibonachchi sonlar ketma-ketligi quyidagicha
aniqlanadi. f1=1; f2=1; fk=fk-2+fk-1,k=3,4,..f1, f2,…,fn elementlari chiqarilsin.
4 1 2 3 5'''
n=int(input('Butun son kiriting: '))
f1,f2=1,1
for i in range(3,n+1):
    f1=f1+f2
    print(f2,f1,end=' ')
    f2=f1+f2