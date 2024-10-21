'''n butun soni berilgan (n>0).
!
1
...
2!
1
1!
1
1
n
   
. Bitta sikldan foydalanib yig‘indi
hisoblansin.
2 2,5'''
n=int(input('Son kiriting:'))
mult=1
sum=1
for i in range(1,n+1):
    mult*=1/i
    sum+=mult
print(sum)