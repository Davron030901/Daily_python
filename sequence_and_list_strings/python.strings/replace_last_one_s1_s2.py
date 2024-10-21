'''s, s1 va s2 satrlar berilgan. s satrdagi oxirgi uchragan s1 qism satr s2 qism satr bilan
almashtirilsin.'''
s=input('Matin kiriting: ')
s1=input('Keyingi Matin kiriting: ')
s2=input('Almastiriluvchi matin kiriting: ')
s=s[::-1]
s1=s1[::-1]
s2=s2[::-1]
if s1 in s:
    s=s.replace(s1,s2,1)
print(s[::-1])