n=int(input("element sonini kiriting:"))
f1=f2=1
l=[f1,f2]
[l.append(l[i-1]+l[i-2]) for i in range(2,n)]
print(l)