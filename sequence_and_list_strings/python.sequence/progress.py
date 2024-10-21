''' n butun son va o‘sish tartibida tartiblangan (joylashtirilgan). n ta butun sondan iborat sonlar
nabori berilgan. Berilgan nabor bir xil elementlarga ega bo‘lishi mumkin. Berilgan tartibda
nabordagi barcha har xil elementlar (bir xil bo‘lmagan elementlar) chiqarilsin.
4ta
5 6 6 8 -------5 6 8'''
mult=[]
b=None
n=int(input('Nechta haqiqiy son kiritmoqchisiz: '))
for i in range(n):
    n=(int(input(f'{i+1}- haqiqiy sonni kiriting:')))
    if n==b:
        continue
    b=n
    mult.append(n)
print(mult)