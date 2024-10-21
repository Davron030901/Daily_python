'''n o‘lchamli butun tipli massiv berilgan. Massivda juft va toq sonlarning(navbat bilan)
almashinib kelishi aniqlansin. Agar almashinib kelsa 0, aks holda qonuniyatni buzgan birinchi
element tartib nomeri chiqarilsin. '''
n = int(input("element sonini kiriting:"))
g=[k for k in range(n,0,-3)]
count=0
for i in range(1,len(g),2):
    if g[i]%2==0 and g[i-1]%2!=0 or g[i]%2!=0 and g[i-1]%2==0:
        count+=1
    else:
        count=i
        break
if count==len(g)//2:
    print(0)
else:
    print(g[count])
