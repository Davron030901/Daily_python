n=int(input("Enter the count: "))
a=int(input("Enter the first element:"))
d=int(input("Enter its difference:"))

massiv=[]
for i in range(n):
    massiv.append(a)
    a += d
print(massiv)
