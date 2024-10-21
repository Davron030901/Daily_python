'''n o‘lchamli butun tipli a massiv berilgan. Uning a1<ak<an qo‘sh tengsizlikni
qanoatlantiradigan oxirgi ak elementining tartib nomeri chiqarilsin.'''
n = int(input("element sonini kiriting:"))
a=[k for k in range(n,0,-1)]
print(a[len(a)//2])