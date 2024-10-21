massive=[13,2,45,1,34,67,0,34,2,34]
N=[]
while len(massive)!=0:
    min=massive[0]
    for i in massive:
        if min>i:
            min=i
        else:
            min=min
    N.append(min)
    massive.remove(min)
print(N)
count=0
for i in N:
    if i%2!=0:
        count+=1
        massive.append(i)

print(f"Massive: {massive},Count: {count}")
