'''Bankdagi boshlang‘ich qo‘yilma summa 1000 so‘m bo‘lsa va u har oyda p foiz ko‘payib borsa
(p-haqiqiy son, 0<p<25) necha oydan so‘ng qo‘yilma 1100 so‘mdan oshishi(o‘tgan oylar soni) k,
hamda qo‘yilmaning oxirgi miqdori s(haqiqiy son) chop etilsin.
7.0 2 1145'''
s=1000
p=float(input('Qo\'yilma foizini kiriting: '))
k=0
while s<1100:
    s+=(s*p)/100
    k+=1
print(k,' ',s)