'''k butun son va k ta bo‘sh bo‘lmagan butun sonli naborlar berilgan. Har bir naborning tugash
simvoli nol (0) sonidan iborat. Har bir nabordagi elementlar soni hamda barcha naborlardagi jami
elementlar soni chiqarilsin.
2
2 6 3 0
5 0
4 2 6'''
k=int(input('Qatorini kiriting: '))
b=[]
a=[]
count=0

for i in range(k):
    m=1
    while m!=0:
        m=(float(input(f'{i+1}qator {count+1} element qiymatini kiriting:')))
        count+=1
    b.append(count)
    count=0
    a=[]
print(b,sum(b))