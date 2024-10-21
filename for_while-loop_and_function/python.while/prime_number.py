'''n(n>1) butun son berilgan. Agar u tub son bo‘lsa true, aks holda false chiqarilsin.
107 True'''
a=int(input('Butun son kiriting: '))
count=0
b=1
while a//2>b:
    if a%b==0:
        count+=1
    b+=1
print(count==1)