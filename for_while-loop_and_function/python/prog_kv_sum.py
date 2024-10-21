'''a va b butun sonlar berilgan. (a<b) a dan b gacha bo‘lgan sonlarning kvadratlar yig‘indisi
topilsin.
1 4 30'''
a=int(input('Son kiriting:'))
b=int(input('Kattaroq son kiriting:'))
sum=0
for i in range(a,b+1):
    sum+=i*i
print(sum)