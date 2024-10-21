'''k, n butun sonlari hamda har birida n tadan element bo‘lgan k ta butun sonlar nabori berilgan.
Berilgan naborlarda 2 yoki 0 elementi bo‘lmasa, ularning 1-elementi chop etilsin, aks holda 0
chiqarilsin.
2 3
2 6 1
5 4 3
0
5'''
k=int(input('Qatorini kiriting: '))
sum=[]
a=[]
n=int(input('Element soni: '))

for i in range(k):
    for j in range(n):
        m=(float(input(f'{i+1}qator {j+1} element qiymatini kiriting:')))
        a.append(m)
    if not(2 or 0) in a:
        sum.append(a[0])
    a=[]
print(sum)