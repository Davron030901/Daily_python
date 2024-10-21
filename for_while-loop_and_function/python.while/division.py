'''n(n>1) butun son berilgan. Bo‘linmaning butunga bo‘lish va qoldiqni aniqlash
operatsiyalaridan foydalanib, sonning o‘ng tomonidan boshlab hamma raqamlari chiqarilsin.
(birlik xonasidan boshlab)
1562 2 6 5 1'''
a=int(input('Butun son kiriting: '))
while a>=1:
    b=a%10
    a//=10
    print(b,end=' ')