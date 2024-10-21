'''c simvol va s, s0 satrlar berilgan. s satrda uchragan har bir c simvolning oldiga s0 satr
joylashtirilsin.'''
s=input('Matin kiriting: ')
s0=input('Keyingi Matin kiriting: ')
c=input('Matinda bor simvol kiriting: ')
S=''
if  c in s:
    for j in range(len(s)):
        if s[j]==c:
            S+=s0
        S+=s[j]
    print(S)
else:
    print("noto'g'ti kiritdingiz")