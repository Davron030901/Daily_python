a=int(input("Enter a: "))
b=int(input("Enter b: "))
if a!=b:
    a=b+a
    b=a
    print(a,",",b,sep="")
else:
    a,b=0,0
    print(b,",",a,sep="")

