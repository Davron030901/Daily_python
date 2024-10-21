'''n o‘lchamli a massiv berilgan. Uning juft indeksli elementlarining ichidan eng kichigi topilsin.'''
n = int(input("element sonini kiriting:"))
g=[k for k in range(n)]
a=min([g[i] for i in range(1,n,2)])
print(a)