'''n(n>0) butun son berilgan. Kvadratdan ildiz chiqarish formulasidan foydalanmay kvadrati n
dan katta eng kichik k soni topilsin. (k
2>n)
5----3'''
n=int(input('son kiriting:'))
k=0
while k**2<n:
    k+=1
print(k)