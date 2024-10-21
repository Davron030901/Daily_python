n=int(input("Enter the count: "))
b=int(input("Enter the first element:"))
q=int(input("Enter its denominator:"))

massiv=[]
for i in range(n):
    massiv.append(b)
    b *= q
print(massiv)
