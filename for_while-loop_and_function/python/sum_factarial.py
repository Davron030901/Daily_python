'''n butun soni berilgan (n>0). 1!+2!+…+n!. Bitta sikldan foydalanib yig‘indi hisoblansin.
4 33'''
n=int(input('Son kiriting:'))
mult=1
sum=0
for i in range(1,n+1):
    mult*=i
    sum+=mult
print(sum)