'''n butun son berilgan. Kvadratdan ildiz chiqarish formulasidan foydalanmay kvadrati n dan katta
bo‘lmagan eng katta butun k soni topilsin. (k
2≤n)
5 2'''
n=int(input('son kiriting:'))
k=0
while k**2<=n:
    k+=1
print(k-1)