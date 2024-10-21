''' n(n>1) butun son berilgan. 3
k<n tengsizlik o‘rinli bo‘ladigan eng katta k butun soni topilsin.
10---- 2'''
n=int(input('son kiriting:'))
k=1
while 3**k<=n:
    k+=1
print(k-1)