n=10000
for i in range(1,n):
    count=0
    for j in range(1,i//2+1):
        if i%j==0:
            count+=j
    if count==i:
        print(i)