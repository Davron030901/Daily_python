'''n o‘lchamli elementlari o‘sish tartibida tartiblangan a va b massivlar berilgan. c massiv
quyidagicha tashkil etilsin: a va b dagi elementlar c ga o‘tkazilsin. c da hosil bo‘lgan
elementlarning o‘sish tartibida bo‘lishi ta`minlansin.
5
0 2 4 6 8
1 3 5 7 9
0 1 2 3 4 5 6 7 8 9'''
n=int(input('element sonini kiriting:'))
a=[k for k in range(0,n,2)]
b=[j for j in range(1,n,2)]
c=[]
print(a,'\n',b)
for i in range(len(a)):
    if a[i]>b[i]:
        c.append(b[i])
        c.append(a[i])
    else:
        c.append(a[i])
        c.append(b[i])
print(c)