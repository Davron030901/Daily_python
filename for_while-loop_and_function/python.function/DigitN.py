'''k butun musbat sonining n-raqamini qaytaradigan (nomerlash o‘ngdan chapga qarab
bajarilgan) butun tipli DigitN(k,n) funksiyasi tasvirlansin. Agar n raqamlar sonidan katta bo‘lsa
funksiya -1 qaytarsin. Berilgan 5 ta butun musbat k1, k2,…k5 sonlari uchun (1, 5) oraliqda
o‘zgaruvchi n soniga mos raqamlar topilsin.
121 34 6 190 50
2
2 3 -1 9 5'''
def DigitN(k):
    while k!=0:
        k=k//10%10
        if k!=0:
            return k
        return -1
for i in range(5):
    print(DigitN(int(input(f'Natural {i+1}sonni kiriting k>0 :'))))