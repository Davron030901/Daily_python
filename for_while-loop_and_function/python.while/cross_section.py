'''a va b musbat sonlar berilgan(a>b). a uzunlikdagi kesmaga b uzunlikdagi kesmani mumkin
qadar eng ko‘p miqdorda joylashtirilganda, a kesmaning bo‘sh (ortib) qolgan bo‘lagi topilsin.
Ko‘paytirish va bo‘lish operatsiyalaridan foydalanilmasin'''
a=int(input('son kiriting:'))
b=int(input('kichik son kiriting:'))
while a>b:
    a-=b
print(a)