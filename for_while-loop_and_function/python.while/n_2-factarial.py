'''n(n>0) butun son berilgan. n ikki factorial hisoblansin. Bu yerda n!!=n(n-2)(n-4)… (oxirgi
ko‘paytuvchi agar n-juft bo‘lsa 2 ga, toq bo‘lsa 1 ga teng.) Butun tip diapozonidan oshib
ketishining oldini olish uchun bu ko‘paytma natija haqiqiy tipli o‘zgaruvchiga qiymatlanadi.
5 ----15'''
n=int(input('son kiriting:'))
count=1
while n>1:
    count*=n
    n-=2
print(count)