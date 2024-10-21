'''. k, n butun sonlari hamda har birida n tadan element bo‘lgan k ta butun sonlar nabori berilgan.
Har bir nabor uchun quyidagi ish amalga oshirilsin: agar nabor 2 soniga ega bo‘lsa uning
elementlar yig‘indisi chiqarilsin. Agar naborda 2 yo‘q bo‘lsa 0(nol) chiqarilsin.
2 3
2 6 1
5 4 3
9
0'''
k=int(input('Qatorini kiriting: '))
b=[]
a=[]
n=int(input('Element soni: '))

for i in range(k):
    for j in range(n):
        m=(float(input(f'{i+1}qator {j+1} element qiymatini kiriting:')))
        a.append(m)
    if 2 in a:
        b.append(sum(a))
    else:
        b.append(0)
    a=[]
print(b)