'''n(n>0) butun son berilgan. Butunga bo‘lish va qoldiqni aniqlash operatsiyalaridan
foydalanib n sonining teskarisiga(o‘ngdan chapga) o‘qishdan hosil qilingan son chiqarilsin.
1562-- 2651'''
a=int(input('Butun son kiriting: '))
while a>=1:
    b=a%10
    a//=10
    print(b,end='')