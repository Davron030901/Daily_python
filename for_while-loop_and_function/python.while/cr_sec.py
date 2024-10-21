'''a va b musbat son berilgan(a>b). a uzunlikdagi kesmaga b uzunlikdagi kesma mumkin qadar
eng ko‘p miqdorda joylashtirilgan bo`lsa, (Ko‘paytirish va bo‘lish operatsiyalaridan foydalanmay)
a kesmaga joylashtirilgan b kesmalar soni aniqlansin.'''
a=int(input('son kiriting:'))
b=int(input('kichik son kiriting:'))
count=0
while a>b:
    a-=b
    count+=1
print(count)