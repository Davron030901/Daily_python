'''n(n>0) butun soni va s satr berilgan. n uzunlikka teng bo‘lgan s satr quyidagi ko‘rinishda
aniqlanadi: agar s satr uzunligi n dan katta bo‘lsa, uning o`ng tomonidan ortiqcha simvollar olib
tashlansin, agar s satr uzunligi n dan kichik bo‘lsa, uning o`ng tomoniga nuqtalar qo‘shilsin.'''
n=int(input('Butun son kiriting:'))
s=input('Matin kiriting: ')
if len(s)>=n:
    for i in range(n):
        print(s[i],end='')
else:
    for j in range(n-len(s)):
        s+='.'
    print(s)