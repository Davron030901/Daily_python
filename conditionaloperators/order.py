a=float(input("Enter a: "))
b=float(input("Enter b: "))
if a>b:
    a,b=b,a
    print(a,",",b,sep="")
else:
    print(b,",",a,sep="")

