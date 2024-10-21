'''k butun son va nol bo‘lmagan butun sonlar nabori berilgan. Uning tugaganlik simvoli nol soni.
Nabordagi k dan katta birinchi son chiqarilsin. Agar bunday son yo‘q bo‘lsa nol chiqarilsin.
3
2 4 3 5 0
4'''
a=[]
k=int(input('Chegara sonni kiriting:'))
n=int(input('haqiqiy sonni kiriting:'))
while n!=0:
    if n!=0 and n>k:
        a.append(n)
    n=int(input('haqiqiy sonni kiriting:'))
print(a[0] if len(a)>=1 else  0)