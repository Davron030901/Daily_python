'''n ta haqiqiy son berilgan. Ularning yig‘indisi topilsin.
1.1 1.2 1.3 1.4 1.5 ---6.5'''
sum=0
n=int(input('Nechta haqiqiy son kiritmoqchisiz: '))
for i in range(n):
    sum+=(float(input(f'{i+1}- haqiqiy sonni kiriting:')))
print(sum)