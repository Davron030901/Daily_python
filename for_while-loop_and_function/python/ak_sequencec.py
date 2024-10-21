n=int(input('Butun son kiriting: '))
a1=1
a2=2
a3=3
print(a1,a2,a3,end=' ')
for i in range(3,n+1,3):
    a1=a3+a2-2*a1
    a2=a1+a3-2*a2
    a3=a2+a1-2*a3
    print(a1,a2,end=' ')