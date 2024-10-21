n=int(input("Enter the count: "))
a=int(input("Enter the first element:"))
b=int(input("Enter the second element:"))
massiv=[a,b]
for i in range(2,n):
    c = 0
    for j in range(len(massiv)):
        c+=massiv[j]
    massiv.append(c)
print(massiv)
