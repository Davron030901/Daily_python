''' k(k>0), n(n>0) butun sonlar va n ta butun sonlardan iborat nabor berilgan. Agar nabor k dan
kichik sonlardan iborat bo‘lsa true, aks holda false chiqarilsin.
5 4
3 2 4 5------ false'''
count=0
k=int(input('Chegarani kiriting: '))
n=int(input('Nechta haqiqiy son kiritmoqchisiz: '))
for i in range(n):
    n=int(input(f'{i+1}- haqiqiy sonni kiriting:'))
    if n>=k:
        count+=1
print(count==0)