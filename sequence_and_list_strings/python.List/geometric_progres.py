n=int(input("element sonini kiriting:"))
b=int(input("1-hadini kiriting:"))
q=int(input("gemetrigini kiriting:"))
l=[b*q**(i-1) for i in range(1,n+1)]
print(l)