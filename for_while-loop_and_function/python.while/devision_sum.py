'''. n(n>1) butun son berilgan. Butunga bo‘lish va qoldiqni aniqlash operatsiyalaridan
foydalanib, uning raqamlari yig‘indisi va raqamlari soni chiqarilsin.
1562 14 4'''
a=int(input('Butun son kiriting: '))
sum=0
count=0
while a>=1:
    b=a%10
    a//=10
    sum+=b
    count+=1
print(sum,count)