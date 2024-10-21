'''▲ s satr va c simvol berilgan. s satrdagi har bir uchragan c simvol ikkilantirilsin'''
s=input('Matin kiriting: ')
c=input('Matinda bor simvol kiriting: ')
S=''
if  c in s:
    for j in range(len(s)):
        S+=s[j]
        if s[j]==c:
            S+=s[j]
    print(S)
else:
    print("noto'g'ti kiritdingiz")