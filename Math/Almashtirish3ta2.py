a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
a=a+b+c
c=a-(b+c)
b=a-(b+c)
a=a-(b+c)
print("a=",a)
print("b=",b)
print("c=",c)