''' 2 ta a va b butun sonlar berilgan. (a<b) a dan b gacha bo‘lgan sonlarning ko‘paytmasi topilsin.
2 5 ----120'''
a=int(input('Son kiriting:'))
b=int(input('Kattaroq son kiriting:'))
mult=1
for i in range(a,b+1):
    mult*=i
print(mult)