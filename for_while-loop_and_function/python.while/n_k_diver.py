'''n va k musbat butun sonlari berilgan. Faqat qo‘shish va ayirish operatsiyasidan foydalanib n ni
k ga bo‘lganda bo‘linmaning butun hamda qoldiq qismi topilsin.
5 2 2 1'''
n=int(input('son kiriting:'))
k=int(input('kichik son kiriting:'))
count=0
while n>k:
    n-=k
    count+=1
print(count,'  ',n)