'''n !! ni hisoblovchi haqiqiy tipli Fact2(n) funksiyasi tasvirlansin.
n !! bu
agar n toq bo‘lsa
n !! 135
...
 n
agar n juft bo‘lsa
n !! 2  4  6 
...
 n
Bu funksiyadan foydalanib berilgan 5 ta butun musbat sonlarning har biri uchun n !! lar
hisoblansin.
6 2 3 4 5 -----48 2 3 8 15'''
import math
def Fact2(n):
    N=1
    if n%2!=0:
        for i in range(1,n+1,2):
            N*=i
    else:
        for i in range(2,n+1,2):
            N*=i
    return N
for i in range(5):
    print(Fact2(int(input('Burchakni kiriting:'))))