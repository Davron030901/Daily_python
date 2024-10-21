'''. k,n butun sonlari va (a1, a2, …, an) n ta haqiqiy sondan iborat nabor berilgan. Berilgan
nabordagi sonlarning har biri uchun k-daraja hisoblansin.
(a1)
k
, (a2)
k
,…, (an)
k
2 4
2.0 3.0 1.0 6.0 -----4.0 9.0 1.0 36.0'''
k=int(input('Darajani kiriting: '))
b=[]
n=int(input('Nechta haqiqiy son kiritmoqchisiz: '))

for i in range(n):
    m=(float(input(f'{i+1}- haqiqiy sonni kiriting:')))
    b.append(m**k)
print(b)