'''k butun soni va nol bo‘lmagan sonli k ta sonlar nabori berilgan. Har bir nabor uchun
quyidagicha harakatlar bajarilsin: Agar nabor elementlari o‘suvchi bo‘lsa 1, kamayuvchi bo‘lsa -
1, kamayuvchi ham o‘suvchi ham bo‘lmasa 0 qiymati chiqarilsin.
3
2 3 5 7
7 1 0
1 3 5
1
-1
1'''
k=int(input('Qatorini kiriting: '))
b=[]
for i in range(k):
    j=0
    t=0
    count=0
    a=[]
    m=1
    while m!=0:
        m=(float(input(f'{i+1}qator {count+1} element qiymatini kiriting:')))
        a.append(m)
        count+=1
        if a[count-2]<a[count-1]:
            j+=1
        elif  a[count-2]>a[count-1]:
            t+=1
    if j==len(a)-2:
        b.append(1)
    elif t==len(a)-1:
        b.append(-1)
    else:
        b.append(0)
print(b)