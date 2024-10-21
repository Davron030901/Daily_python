m=int(input('Satrdagi elementlar sonini kiriting:'))
n=int(input('Satrlar sonini kiriting:'))
satr=[]

for i in range(1,m+1):
    s=[]
    for j in range(1,n+1):
        s.append(5*j)
    satr.append(s)
print(satr)