massive=[13,2,45,1,34,67,0,34,2,34]
p=[]
m=[]
count=0
for i in massive:
    if i%2==0:
        p.append(count)
    else:
        m.append(count)
    count+=1
m.reverse()
print(f"Positive index: {p}, Negative index: {m}")