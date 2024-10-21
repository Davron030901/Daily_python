'''Nol bo‘lmagan butun sonli n o‘lchamli massiv berilgan. Uning elementlari geometrik
progresssiyani tashkil etishi tekshirilsin. Agar tashkil etsa progressiya maxraji aks holda 0(nol)
chiqarilsin.
4
16 8 4 2
 0.5'''
n = int(input("element sonini kiriting:"))
g=[16*2**(-k) for k in range(1,n+1)]
if (g[1]/g[0])==(g[len(g)-1]/g[len(g)-2]):
    print(g[1]/g[0])
else:
    print(0)