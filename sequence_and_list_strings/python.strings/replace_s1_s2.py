'''. s, s1 va s2 satrlar berilgan. s satrdagi 1-uchragan s1 qism satr s2 qism satr bilan almashtirilsin'''
s=input('Matin kiriting: ')
s1=input('Keyingi Matin kiriting: ')
s2=input('Almastiriluvchi matin kiriting: ')
if s1 in s:
    s=s.replace(s1,s2,1)
print(s)