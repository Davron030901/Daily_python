'''2 ta a va b butun sonlar berilgan. (a<b) a dan b gacha bo‘lgan butun sonlar yig‘indisi topilsin.
2 5--- 14'''
a=int(input('Son kiriting:'))
b=int(input('Kattaroq son kiriting:'))
sum=0
for i in range(a,b+1):
    sum+=i
print(sum)