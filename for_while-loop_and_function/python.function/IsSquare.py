'''Berilgan butun k(k>0) parametr, biror butun sonning kvadratiga teng bo‘lsa “true” aks holda
“false” qiymat qaytaruvchi mantiqiy tipli IsSquare(k) funksiyasi tasvirlansin. Bu funksiyadan
foydalanib berilgan 10 ta butun sondan iborat nabordagi to‘la kvadrat bo‘lgan sonlar miqdori
aniqlansin.
1 2 3 4 5 6 7 8 9 10------ 2'''
count=0
def IsSquare(k):
    return k**2
n=[]
m=[]
for i in range(10):
    n.append(int(input(f'Natural {i+1}sonni kiriting k>0 :')))
    m.append(IsSquare(n[i]))
    if n[i] in m:
        count+=1
print(count)