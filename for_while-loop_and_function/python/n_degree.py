'''a va n sonlari berilgan. Bitta sikldan foydalanib a sonining 1 dan n gacha bo‘lgan darajalari
chiqarilsin.
2 3 2 4 8'''
a=int(input('Son kiriting:'))
n=int(input('son soni kiriting:'))
mult=1
for i in range(1,n+1):
    print(a**i,end=' ')