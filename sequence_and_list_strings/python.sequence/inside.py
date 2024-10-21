'''n(n>2) butun soni va n ta haqiqiy sondan iborat nabor berilgan. Naborning ichki elementlari
katta chetki elementlari kichik bo‘lsa 0, aks holda 1 elementi chiqarilsin.
5
3.1 2.1 1.9 2.2 5.6 -----0'''
count=0
b=[]
n=int(input('Nechta haqiqiy son kiritmoqchisiz: '))
for i in range(n):
    m=(float(input(f'{i+1}- haqiqiy sonni kiriting:')))
    b.append(m)
    if i>1 and b[0]>b[i-1] and b[i-1]<b[-1]:
        count+=1
print(int(count==0))