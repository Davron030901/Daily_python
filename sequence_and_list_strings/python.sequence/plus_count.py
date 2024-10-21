'''Nol bo‘lmagan butun sonlar nabori berilgan. Uning tugaganlik simvoli(alomati) nol soni.
Berilgan nabordagi barcha musbat juft sonlar yig‘indisi chiqarilsin. Agar naborda talab qilingan
son yo‘q bo‘lsa nol (0) chiqarilsin.
5 3 7 9 0 ----0'''
count=0
n=int(input('haqiqiy sonni kiriting:'))
while n!=0:
    if n>0 and n%2==0:
        count+=n
    n=int(input('haqiqiy sonni kiriting:'))
print(count)