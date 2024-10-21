n=int(input('son kiriting:'))
f1=1
f2=1
while f1<n and f2<n:
    f1=f1+f2
    f2=f1+f2
print(f1) if f1>n else print(f2)