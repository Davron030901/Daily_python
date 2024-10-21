'''k butun soni va nol bo‘lmagan sonli k ta sonlar nabori berilgan. Har bir nabor kamida 3 tadan
elementni saqlaydi, har bir nabor uchun quyidagicha harakatlar bajarilsin: agar nabor elementlari
arrasimon bo‘lsa uning elementlari soni, boshqa vaziyatlarda uning birinchi elementi chop etilsin.
3
5 4 6 5
3 4 5
5 2 3 1
4
3
4'''
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
        b.append(a[0])
    elif t==len(a)-1:
        b.append(a[0])
    else:
        b.append(len(a))
print(b)