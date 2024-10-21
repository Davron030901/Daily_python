'''Kvadrat tenglamaning ildizlari sonini aniqlaydigan RootsCount(a,b,c) butun tipli funksiya
tasvirlansin(a, b, c- haqiqiy parametr a≠0). Bu funksiyadan foydalanibberilgan 3 ta kvadrat
tenglamaning har biri uchun ildizlari soni aniqlansin.
1 -5 6
1 -4 4
1 4 6
2
1 '''
def RootsCount(a,b,c):
    D=b**2-4*a*c
    if D<0:
        return 0
    elif D==0:
        return 1
    else:
        return 2
a=float(input('1-hadini kiriting:'))
b=float(input('2-hadini kiriting:'))
c=float(input('3-hadini kiriting:'))
print(RootsCount(a,b,c))