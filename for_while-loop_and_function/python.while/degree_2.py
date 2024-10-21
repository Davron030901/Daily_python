'''n(n>0) butun son berilgan. U 2 ning biror bir darajasidan iborat bo‘lsa n=2k
, shu darajaning
ko‘rsatkichi k butun soni topilsin.
128 7'''
n=int(input('son kiriting:'))
k=2
count=0
while n>=k:
    n/=k
    count+=1
if n==1:
    print(count)
else:
    print('ikkining darajasi emas')