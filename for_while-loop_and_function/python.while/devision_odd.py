'''n(n>0) butun son berilgan. Butunga bo‘lish va qoldiqni aniqlash operatsiyalaridan foydalanib
n sonida toq raqam borligi aniqlansin. Agar bor bo‘lsa true, aks holda false chiqarilsin.
1668 True'''
a=int(input('Butun son kiriting: '))
count=0
while a>=1:
    b=a%10
    a//=10
    if b%2==1:
        count+=1
print(count!=0)