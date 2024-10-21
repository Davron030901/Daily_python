'''a va n sonlari berilgan.1-a+a2
-a
3+…+(-1)na
n
. Bitta sikldan foydalanib ifodaning qiymati
hisoblansin. Hisoblashda shart operatoridan foydalanilmasin.
2 4 11'''
a=int(input('Son kiriting:'))
n=int(input('Darajani kiriting:'))
sum=0
for i in range(n+1):
    sum+=((-1)**i)*(a**i)
print(sum)