'''n butun son berilgan. Butunga bo‘lish va qoldiqini aniqlash operatsiyalaridan foydalanib n
sonida “2” raqami borligi aniqlansin. Agar bor bo‘lsa “true” aks holda “false” chiqarilsin.
1562 True'''
a=int(input('Butun son kiriting: '))
count=0
while a>=1:
    b=a%10
    a//=10
    if b==2:
        count+=1
print(count!=0)