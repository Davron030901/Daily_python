def  IsPrime(k):
    if k==2:
        return k
    for i in range(2,k//2+1):
        if k%i==0:
            break
        return k
count=0
n=[]
m=[]
for i in range(10):
    n.append(int(input(f'Natural {i+1}sonni kiriting k>0 :')))
    m.append(IsPrime(n[i]))
    if n[i] in m:
        count+=1
print(count)