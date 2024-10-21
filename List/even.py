n=int(input("Enter the count: "))
a=int(input("Enter the first element:"))
d=int(input("Enter its difference:"))

massiv=[]
for i in range(n):
    massiv.append(a)
    a += d
print(massiv)
N=[]
count=0
for i in massiv:
    if i%2==0:
        count+=1
        N.append(i)

print(f"Massive: {N},Count: {count}")
