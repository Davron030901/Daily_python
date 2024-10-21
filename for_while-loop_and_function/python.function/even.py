'''Agar berilgan butun son juft bo‘lsa “true” aks holda “false” qiymat qaytaruvchi mantiqiy tipli
Even(k) funksiyasi tasvirlansin. Bu funksiyadan foydalanib, berilgan 10 ta butun sondan iborat
nabordagi juft sonlarning miqdori topilsin.
1 2 3 4 5 6 7 8 9 10 5'''
def Even(k):
    if k%2==0:
        return 1
    else:
        return 0
count=0
for i in range(10):
    count+=Even(int(input('Butun son kiriting:')))
print(count)