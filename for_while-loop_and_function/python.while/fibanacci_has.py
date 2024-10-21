'''n(n>1) butun son berilgan. fk Fibonachchi sonlar ketma-ketligi quyidagicha aniqlanadi. f1=1,
f2=1, fk=fk-2+fk-1 k=3, 4….
n=fk bo‘lsa fk+1 va fk-1(oldingi va keyingi) Fibonachchi sonlari chiqarilsin, aks holda 0 chiqarilsin.
13----  8 --21'''
n=int(input('son kiriting:'))
f1=1
f2=1
count=0
while f1<n and f2<n:
    f1=f1+f2
    f2=f1+f2
    if f1==n or f2==n:
        count+=1
if count==1:
    if f2==n:
        print(f2-f1,f1+f2)
    else:
        print(f2-f1,f2)
else:
    print(0)