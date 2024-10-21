''' butun son va nol bo‘lmagan butun sonlar nabori berilgan. Uning tugaganlik simvoli nol soni.
Naborda k dan katta oxirgi son chiqarilsin. Agar bunday son yo‘q bo‘lsa nol chiqarilsin.
4
2 1 5 7 0
7'''
count=0
k=int(input('Chegara sonni kiriting:'))
n=int(input('haqiqiy sonni kiriting:'))
while n!=0:
    if n!=0 and n>k:
        count=n
    n=int(input('haqiqiy sonni kiriting:'))
print(count)