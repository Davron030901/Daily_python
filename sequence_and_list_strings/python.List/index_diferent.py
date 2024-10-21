'''n o‘lchamli butun sonli massiv berilgan. Berilgan massivdagi har xil elementlar soni topilsin.'''
import random
n=int(input('element sonini kiriting:'))
g=[random.randint(1,n-2) for _ in range(n)]
print(g)
a=[]
for j in range(len(g)):
    for i in range(j+1,len(g)):
        if g[j]==g[i]:
            a.append(i)
    if len(a)!=0:
        a.insert(0,j)
        break
print(len(g)-len(a)+1)