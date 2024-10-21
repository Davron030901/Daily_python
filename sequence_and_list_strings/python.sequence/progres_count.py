'''n butun soni va n ta haqiqiy sondan iborat nabor berilgan. Berilgan nabor o‘suvchi ketmaketlikni tashkil etishini tekshiring. Agar tashkil etsa true, tashkil etmasa(aks holda) false
chiqarilsin.
4
2.1 5.6 8.8 -------true'''
count=0
b=[]
n=int(input('Nechta haqiqiy son kiritmoqchisiz: '))
for i in range(n):
    n=(float(input(f'{i+1}- haqiqiy sonni kiriting:')))
    b.append(n)
    if b[i-1]>b[i]:
        count+=1
print(count==0)