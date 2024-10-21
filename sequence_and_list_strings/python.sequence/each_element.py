'''k, n butun sonlari hamda har birida n tadan element bo‘lgan k ta butun sonlar nabori berilgan.
Har bir nabordagi elementlar yig‘indisi chiqarilsin.
2 3
5 4 2
2 6 1
11 9'''
k=int(input('Qatorini kiriting: '))
sum=0
a=[]
b=[]
n=int(input('Element soni: '))

for i in range(k):
    for j in range(n):
        m=(float(input(f'{i+1}qator {j+1} element qiymatini kiriting:')))
        a.append(m)
        sum+=m
    b.append(sum)
    a=[]
    sum=0
print(b)