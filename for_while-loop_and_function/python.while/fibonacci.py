'''n(n>1) butun son berilgan. fk Fibonachchi sonlar ketma-ketligi quyidagicha aniqlansa, f1=1,
f2=1, fk=fk-2+fk-1 k=3, 4…,
n sonining Fibonachchi sonlar ketma-ketligida uchrashi tekshirilsin. Agar n soni uchrasa true, aks
holda false chiqarilsin.
7 False'''
n=int(input('son kiriting:'))
f1=1
f2=1
count=0
while f1+f2<=n:
    f1=f1+f2
    f2=f1+f2
    if f1==n or f2==n:
        count+=1
print(count==1 or n==1)