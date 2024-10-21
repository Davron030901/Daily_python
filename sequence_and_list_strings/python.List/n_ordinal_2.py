'''n o‘lchamli nol bo‘lmagan butun tipli massiv berilgan. Musbat va manfiy sonlarning
almashinib kelishi tekshirilsin. Agar almashinib kelsa 0 aks holda qonuniyatni buzgan birinchi
elementning tartib nomeri chiqarilsin.'''
n = int(input("element sonini kiriting:"))
g=[k for k in range(n)]
count=0
for i in range(1,len(g),2):
    if g[i]<0 and g[i-1]>0 or g[i]>0 and g[i-1]<0:
        count+=1
    else:
        count=i
        break
if count==len(g)//2:
    print(0)
else:
    print(g[count])