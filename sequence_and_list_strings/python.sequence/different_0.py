'''k butun son va nol bo‘lmagan butun sonlar nabori berilgan. Uning tugaganlik simvoli nol soni
naborda k dan kichkina noldan farqli sonlar miqdori chiqarilsin.
3 1 2 4 6 0 2'''
count=0
k=int(input('Chegara sonni kiriting:'))
n=int(input('haqiqiy sonni kiriting:'))
while n!=0:
    if n!=0 and n<k:
        count+=1
    n=int(input('haqiqiy sonni kiriting:'))
print(count)