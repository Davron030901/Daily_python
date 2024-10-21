'''n(n>0) butun son va n ta haqiqiy sonlardan iborat nabor berilgan. Berilgan nabordagi barcha
sonlarning butun qismlari hamda butun qismlarining yig‘indisi chiqarilsin.
3
3.5 2.6 8.7 -------3 2 8 13'''
sum=0
mult=[]
n=int(input('Nechta haqiqiy son kiritmoqchisiz: '))
for i in range(n):
    n=(float(input(f'{i+1}- haqiqiy sonni kiriting:')))
    sum+=int(n)
    mult.append(int(n))
print(mult,' ',sum)