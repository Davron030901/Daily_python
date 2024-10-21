'''Butun musbat n1, n2 sonlar va s1, s2 satrlar berilgan. Bu satrlardan foydalanib yangi s satr hosil
qilinsin: s satrning dastlabki n1 ta simvoli s1 satrning bosh qismidan, oxirgi n2 ta simvoli s2 satrning
oxiridan iborat bo‘lsin. '''
n1=int(input('1-Butun son kiriting:'))
s1=input('1-Matin kiriting butun son uzunligicha: ')
n2=int(input('2-Butun son kiriting:'))
s2=input('2-Matin kiriting butun son uzunligicha: ')
s=''
if len(s1)>=n1 and len(s1)>=n1:
    for i in range(n1):
        s+=s1[i]
    for j in range(len(s2)-n2,len(s2)):
        s+=s2[j]
    print(s)
else:
    print("noto'g'ti kiritdingiz")