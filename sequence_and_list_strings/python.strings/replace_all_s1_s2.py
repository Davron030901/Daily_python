'''s, s1 va s2 satrlar berilgan. s satrda uchragan barcha s1 qism satrlar s2 qism satr bilan
almashtirilsin.'''
s=input('Matin kiriting: ')
s1=input('Keyingi Matin kiriting: ')
s2=input('Almastiriluvchi matin kiriting: ')
if s1 in s:
    s=s.replace(s1,s2)
print(s)