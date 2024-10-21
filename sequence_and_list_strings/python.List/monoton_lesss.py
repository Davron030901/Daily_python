'''. n o‘lchamli massiv berilgan. Uning monoton kamayuvchi bo‘laklari soni topilsin'''
import random
n=int(input('element sonini kiriting:'))
g=[random.randint(1,n) for _ in range(n)]
print(g)
count=0
for i in range(1,len(g)):
    if len(g)-1==i:
        break
    if g[i-1]>g[i]:
        count+=1
print(count)
