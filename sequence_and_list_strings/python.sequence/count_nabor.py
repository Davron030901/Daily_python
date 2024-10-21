'''k butun soni va nol bo‘lmagan sonli k ta sonlar nabori berilgan. Har bir nabor kamida 2 tadan
elementni saqlaydi, naborning oxirgi simvoli nol (0) hisoblanadi. Elementlari o‘sish yoki
kamayish tartibida joylashgan(0 hisobga olinmaydi) naborlar soni topilsin.
3
2 3 5 0
7 1 0
1 3 0
3'''
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
    if j==len(a)-2 or t==len(a)-2:
        b.append(1)
print(sum(b))