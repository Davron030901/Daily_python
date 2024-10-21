'''n butun soni va a1, a2, …, an lardan iborat haqiqiy sonlar nabori berilgan. Sonlar quyidagicha
chiqarilsin.
a1, a2
2
,…, an-1
n-1
, an
n
3
3.0 2.0 2.0 3.0 4.0 8.0 '''
k=int(input('Darajani kiriting: '))
b=[]
n=int(input('Nechta haqiqiy son kiritmoqchisiz: '))

for i in range(n):
    m=(float(input(f'{i+1}- haqiqiy sonni kiriting:')))
    b.append(m**(i+1))
print(b)