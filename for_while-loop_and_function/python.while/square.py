'''a,b,c musbat sonlar berilgan. axb o‘lchamli to‘g‘ri to‘rtburchakka tomoni c bo‘lgan
kvadratlar mumkin bo‘lgan eng ko‘p miqdorda joylashtirilsa, ko‘paytirish va bo‘lish
operatsiyalaridan foydalanmay to‘g‘ri to‘rtburchakka joylashtirilgan kvadratlar soni aniqlansin.
5 10 2 10'''
a=int(input('Son kiriting: '))
b=int(input('Son kiriting: '))
c=int(input('Son kiriting: '))

count_a=0
count_b=0
while a>=c :
    a-=c
    while b>=c:
        b-=c
        count_b+=1
    count_a+=count_b
print(count_a)


# count_a = 0
# while a >= c:
#     count_a+=1
#     a -=c
# count_b = 0
# while b >= c:
#     count_b+=1
#     b -=c
# count = 0
# while count_a !=0:
#     count+=count_b
#     count_a -=1


# # print(count_a, count_b)
# print(count)
