'''n(n>1) butun son berilgan. fk Fibonachchi sonlar ketma-ketligi quyidagicha aniqlanadi. f1=1,
f2=1, fk=fk-2+fk-1 k=3, 4…
n=fk bo‘lsa, k (Fibonachchi sonining tartib nomeri) chiqarilsin, aks holda 0 chiqarilsin'''
n=int(input('son kiriting:'))
f1=1
f2=1
count=2
while f1<n and f2<n:
    f1=f1+f2
    count+=1
    if f1==n:
        break
    f2=f1+f2
    count+=1
if f1==n or f2==n:
    print(count)
else:
    print(0)