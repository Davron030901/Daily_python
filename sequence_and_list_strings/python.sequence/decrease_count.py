'''n(n>1) butun soni va n ta haqiqiy sondan iborat nabor berilgan. Agar berilgan nabor
kamayuvchi ketma-ketlikni tashkil etsa 0, aks holda(qonuniyat buzilsa) 1 chiqarilsin.
3
1.1 5.3 4.2 ----1'''
count=0
b=[]
n=int(input('Nechta haqiqiy son kiritmoqchisiz: '))
for i in range(n):
    n=(float(input(f'{i+1}- haqiqiy sonni kiriting:')))
    b.append(n)
    if b[i-1]<b[i]:
        count+=1
print(int(count!=0))