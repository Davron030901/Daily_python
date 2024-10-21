'''n(n>0) butun son va n ta haqiqiy sonlardan iborat nabor berilgan. Berilgan nabordagi sonlar
yig‘indisi va ko‘paytmasi chiqarilsin.
3
2.5 2.0 1.0 ---------5.5 5'''
sum=0
mult=1
n=int(input('Nechta haqiqiy son kiritmoqchisiz: '))
for i in range(n):
    n=(float(input(f'{i+1}- haqiqiy sonni kiriting:')))
    sum+=n
    mult*=n
print(sum,' ',mult)