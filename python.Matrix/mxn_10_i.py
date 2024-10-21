'''m va n butun musbat sonlar berilgan. Massivning 1-satridagi har bir elementiga 10*i(i=1,…,
m) qiymatlarni joylashtirish bilan
m  n
o‘lchamli butun sonli matritsa tashkil etilsin. '''
m=int(input('Satrdagi elementlar sonini kiriting:'))
n=int(input('Satrlar sonini kiriting:'))
satr=[]

for i in range(1,m+1):
    s=[]
    for j in range(1,n+1):
        s.append(10*j)
    satr.append(s)
print(satr)