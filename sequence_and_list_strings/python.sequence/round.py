sum=0
mult=[]
n=int(input('Nechta haqiqiy son kiritmoqchisiz: '))
for i in range(n):
    n=round(float(input(f'{i+1}- haqiqiy sonni kiriting:')))
    sum+=n
    mult.append(n)
print(mult,' ',sum)