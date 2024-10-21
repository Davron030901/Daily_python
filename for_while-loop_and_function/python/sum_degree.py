'''a va n sonlari berilgan.
n
1 a  a  a  ...  a
2 3
. Bitta sikldan foydalanib yig‘indi
hisoblansin.
3 3 40'''
a=int(input('Son kiriting:'))
n=int(input('Darajani kiriting:'))
sum=0
for i in range(n+1):
    sum+=a**i
print(sum)