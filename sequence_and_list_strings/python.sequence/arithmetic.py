'''n ta haqiqiy sonlar berilgan. Ularning o‘rta arifmetigi topilsin.
2.0 3.0 5.0 4.0 1.0 ---------3.0'''
arithmetic=0
n=int(input('Nechta haqiqiy son kiritmoqchisiz: '))
for i in range(n):
    arithmetic+=(float(input(f'{i+1}- haqiqiy sonni kiriting:')))
print(arithmetic/n)