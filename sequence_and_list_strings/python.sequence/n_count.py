'''b haqiqiy son, n butun son va n ta haqiqiy sonlar nabori berilgan. Chiqariladigan sonlar tartibini
saqlagan holda b sonidan boshlab (undan keyingi) nabor elementlari chiqarilsin.
3.3 4 1.2 1.0 3.3 2.1 -----3.3 2.1'''
mult=[]
count=0
b=float(input('Chegarani kiriting: '))
n=int(input('Nechta haqiqiy son kiritmoqchisiz: '))
for i in range(n):
    n=(float(input(f'{i+1}- haqiqiy sonni kiriting:')))
    if n==b or count!=0:
        mult.append(n)
        count=1
print(mult)