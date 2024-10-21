'''n butun soni berilgan
1,11,21.3
...1,n
(n ta ko‘paytuvchi). Ko‘paytma hisoblansin.
2 1.32'''
n=int(input('Son kiriting:'))

mult=1
for i in range(1,n+1):
    mult*=(1+i/10)
print(mult)