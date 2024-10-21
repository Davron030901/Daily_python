'''Butun k parametr palindrom bo‘lsa true aks holda false qiymat qaytaradigan mantiqiy tipli
Ispalindron(K) funksiyasi tasvirlansin. (palendrom son – o‘ng va chapdan bir xil o‘qiladigan
sondir). Funksiyani tasvirlashda Digit count va Digit N funksiyalaridan foydalanish mumkin. Bu
funksiyadan foydalanib berilgan 5 ta butun musbat sondan iborat nabordagi palendrom sonlar
miqdori aniqlansin.
123 22 101 21 64------ 2'''
def Ispalindron(k) :
    K=k
    n=0
    N=int(len(str(k)))
    while k!=0:
        n+=k%10*10**(N-1)
        N-=1
        k=k//10
    if n==K:
        return 1
    else:
        return 0
count=0
for i in range(5):
    count+=Ispalindron(int(input(f'Natural {i+1}sonni kiriting k>0 :')))
print(count)