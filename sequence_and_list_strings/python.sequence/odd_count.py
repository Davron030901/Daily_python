'''n(n>0) butun son va n ta butun sondan iborat nabor berilgan. Berilgan nabordagi barcha toq
sonlar va ularning miqdori k chiqarilsin.
4
3 6 4 5------- 3 5 2'''
count=0
mult=[]
n=int(input('Nechta haqiqiy son kiritmoqchisiz: '))
for i in range(n):
    n=int(input(f'{i+1}- haqiqiy sonni kiriting:'))
    if n%2!=0:
        count+=1
        mult.append(n)
print(mult,' ',count)