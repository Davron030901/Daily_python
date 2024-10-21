'''n butun soni va a1, a2, …, an lardan iborat haqiqiy sonlar nabori berilgan. Sonlar quyidagicha
chiqarilsin. a1
n
, a2
n-1
,…, an-1
2
, an
3
3.0 2.0 2.0 ----27.0 4.0 2.0 '''
k=int(input('Darajani kiriting: '))
b=[]
n=int(input('Nechta haqiqiy son kiritmoqchisiz: '))

for i in range(n):
    m=(float(input(f'{i+1}- haqiqiy sonni kiriting:')))
    b.append(m**(n-i))
print(b)