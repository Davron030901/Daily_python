''' Bir xil sonlarni o‘z ichiga olmaydigan n o‘lchamli butun tipli massiv berilgan. Uning
elementlari arifmetik progressiyani tashkil etishi aniqlansin. Agar tashkil etsa progressiya
ayirmasi, tashkil etmasa 0(nol) chiqarilsin.
6 --3 8 13 18 23 28 ---5'''
n = int(input("element sonini kiriting:"))
a=[3+5*k for k in range(n)]
if (a[1]-a[0])==(a[len(a)-1]-a[len(a)-2]):
    print(a[1]-a[0])
else:
    print(0)