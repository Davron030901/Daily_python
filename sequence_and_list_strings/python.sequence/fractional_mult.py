'''n(n>0) butun soni va n ta musbat haqiqiy sonlar nabori berilgan. Berilgan nabordagi barcha
sonlarning kasr qismlari hamda hamma kasr qismlarining ko‘paytmasi chiqarilsin.
3
3.2 2.5 8.5 -------2 5 5 50'''
mult=[]
multiplication=1
n=int(input('Nechta haqiqiy son kiritmoqchisiz: '))
for i in range(n):
    n=(float(input(f'{i+1}- haqiqiy sonni kiriting:')))
    n=(n-int(n))*10
    multiplication*=n
    mult.append(n)
print(mult,' ',multiplication)