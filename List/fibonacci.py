n=int(input("Enter the count>2 : "))


massiv=[1,1]
for i in range(2,n):
    massiv.append(massiv[i-1]+massiv[i-2])
print(massiv)
