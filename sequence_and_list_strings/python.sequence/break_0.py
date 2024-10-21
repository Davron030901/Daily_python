'''Nol bo‘lmagan butun sonlar nabori berilgan. Uning tugaganlik simvoli(alomati) nol soni.
Nabordagi (noldan farqli) sonlar miqdori chiqarilsin.
5 3 2 6 0 4'''
count=0
n=int(input('haqiqiy sonni kiriting:'))
while n!=0:
    if n!=0:
        count+=1
    n=int(input('haqiqiy sonni kiriting:'))
print(count)