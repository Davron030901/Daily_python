'''k, n butun sonlari hamda har birida n tadan element bo‘lgan k ta butun sonlar nabori berilgan.
2 soniga ega bo‘lgan naborlar miqdori topilsin. Agar bunday nabor yo‘q bo‘lsa 0(nol) chiqarilsin.
2 3
2 6 1
5 4 3
1'''
k=int(input('Qatorini kiriting: '))
sum=0
a=[]
n=int(input('Element soni: '))

for i in range(k):
    for j in range(n):
        m=(float(input(f'{i+1}qator {j+1} element qiymatini kiriting:')))
        a.append(m)
    if 2 in a:
        sum+=1
    a=[]
print(sum)