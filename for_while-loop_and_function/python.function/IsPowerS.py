'''. Berilgan butun k (k>0) parametr, 5 ning biror darajasiga teng bo‘lsa true aks holda false
qiymatini qaytaruvchi mantiqiy tipli IsPowerS(k) funksiyasi tasvirlansin. Bu funksiyadan 
foydalanib berilgan 10 ta butun sondan iborat nabordagi 5 ning darajalariga teng bo‘lgan
sonlarning miqdori topilsin.
1 2 3 4 5 6 7 8 9 10 --- 2'''
count=0
N=int(input('Son kiriting:'))
def  IsPowerN(k):
    return N**i
n=[]
m=[]
for i in range(10):
    n.append(int(input(f'Natural {i+1}sonni kiriting k>0 :')))
    m.append(IsPowerN(i))
    if n[i] in m:
        count+=1
print(count)