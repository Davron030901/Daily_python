a,b,c=int(input("Enter number a=")),int(input('Enter number b=')),int(input("Enter number c="))
print((not(a==b and b==c))and(a>0 and b>0 and c>0)and (a==b or b==c or c==a))