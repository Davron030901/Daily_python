a=int(input("Enter three room different number a="))
b=(a%100)%10
c=a//100
d=a//10-c*10
print(b!=c and c!=d and b!=d)