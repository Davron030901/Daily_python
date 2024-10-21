'''. n(n>0) butun son va n ta butun sondan iborat nabor berilgan. Agar nabor musbat sonlardan
iborat bo‘lsa true, aks holda false chiqarilsin.
3
5 6 -4 ----false'''
count=0
n=int(input('Nechta haqiqiy son kiritmoqchisiz: '))
for i in range(n):
    n=int(input(f'{i+1}- haqiqiy sonni kiriting:'))
    if n<=0:
        count+=1
print(count==0)