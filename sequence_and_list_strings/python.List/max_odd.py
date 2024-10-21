'''n o‘lchamli a massiv berilgan. Uning toq indeksli elementlarining ichidan eng kattasi topilsin.'''
n = int(input("element sonini kiriting:"))
g=[k for k in range(n)]
a=max([g[i] for i in range(0,n,2)])
print(a)