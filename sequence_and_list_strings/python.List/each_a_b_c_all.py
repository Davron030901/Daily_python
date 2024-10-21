'''Elementlari kamayish bo‘yicha tartiblangan 3 ta butun tipli mos ravishda na, nb, nc o‘lchamli
a, b va c massivlar berilgan. Bu massivlarni natijaviy d (na+nb+nc o‘lchamli) massivga kamayish
bo‘yicha tartiblab birlashtirilsin.
3
3 2 1
5 4 0
9 8 6
9 8 6 5 4 3 2 1 0'''
n=1
while n%3!=0:
    n=int(input('element sonini kiriting(3ga karrali):'))
a=[k for k in range(n,0,-3)]
b=[j for j in range(n-1,0,-3)]
c=[l for l in range(n-2,0,-3)]
d=[]
print(a,'\n',b,'\n',c)
for i in range(len(a)):
    if a[i]>b[i]:
        if b[i]>c[i]:
            d.append(a[i])
            d.append(b[i])
            d.append(c[i])
        else:
            d.append(a[i])
            d.append(c[i])
            d.append(b[i])
    else:
        if a[i]>c[i]:
            d.append(b[i])
            d.append(a[i])
            d.append(c[i])
        else:
            d.append(b[i])
            d.append(c[i])
            d.append(a[i])
print(d)