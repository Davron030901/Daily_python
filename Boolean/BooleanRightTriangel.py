a,b,c=int(input("Enter number a=")),int(input('Enter number b=')),int(input("Enter number c="))
print((a>0 and b>0 and c>0)and (a+b>c and b+c>a and a+c>b) and ((a**2+b**2)**0.5==c or (a**2+c**2)**0.5==b or (c**2+b**2)**0.5==a))