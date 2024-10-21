'''n(n>0) butun soni va n ta butun sondan iborat nabor berilgan. Berilgan nabordagi hamma juft
sonlar va ularning miqdori k chiqarilsin.
4
3 6 4 5--- 6 4 ---2'''
count=0
mult=[]
n=int(input('Nechta haqiqiy son kiritmoqchisiz: '))
for i in range(n):
    n=int(input(f'{i+1}- haqiqiy sonni kiriting:'))
    if n%2==0:
        count+=1
        mult.append(n)
print(mult,' ',count)