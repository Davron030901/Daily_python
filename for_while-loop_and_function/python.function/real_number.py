'''Berilgan x haqiqiy soni uchun
x<0 da -1
x=0 da 0 va
x>0 da 1
qiymat qaytaruvchi butun tipli sign(x) funksiyasi tasvirlansin. Bu funksiyadan foydalanib berilgan
a va b sonlari uchun mos qiymatlar olinsin.
-3 3 -1 1'''
def sign(x):
    if x<0:
        return(-1)
    elif x==0:
        return 0
    else:
        return 1
a=float(input('Haqiqiy son kiriting:'))
b=float(input('2-Haqiqiy son kiriting:'))
print(sign(a),sign(b))