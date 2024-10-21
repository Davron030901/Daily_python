'''a va b butun musbat sonlari berilgan. Evklid algoritmidan foydalanib ularning eng katta
umumiy bo‘luvchisi topilsin (EKUB). Agar b≠0 bo‘lsa
EKUB(a,b)=EKUB(b,a mod b) aks holda EKUB(a,0)=a.
24 and 38 ---2'''
a=int(input('Butun son kiriting: '))
b=int(input('Butun son kiriting: '))
while a%b!=0 and b%a!=0:
    if a>b:
        a=a%b
    else:
        b=b%a
print(a) if a%a==0 and b%a==0 else print(b)