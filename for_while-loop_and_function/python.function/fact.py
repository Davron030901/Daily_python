'''n faktorialni hisoblovchi haqiqiy tipli Fact(n) funksiyasi tasvirlansin. Bu funksiyadan
foydalanib berilgan 5 ta butun musbat sonning har biri uchun faktoriallar hisoblansin.
1 2 3 4 5 ----1 2 6 24 120 '''
import math
def Fact(n):
    N=1
    for i in range(1,n+1):
        N*=i
    return N
for i in range(5):
    print(Fact(int(input('Burchakni kiriting:'))))