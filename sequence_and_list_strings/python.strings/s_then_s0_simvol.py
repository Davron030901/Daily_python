'''c simvol va s, s0 satrlar berilgan. s satrda uchragan har bir c simvoldan keyinga s0 satr
joylashtirilsin.'''
s=input('Matin kiriting: ')
s0=input('Keyingi Matin kiriting: ')
c=input('Matinda bor simvol kiriting: ')
S=''
if  c in s:
    for j in range(len(s)):
        S+=s[j]
        if s[j]==c:
            S+=s0
    print(S)
else:
    print("noto'g'ti kiritdingiz")