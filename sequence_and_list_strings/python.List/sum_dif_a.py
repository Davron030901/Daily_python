'''n o‘lchamli massiv hamda k va l butun sonlari berilgan. (1≤k≤l≤n). k-indeksdan l-indeksgacha
bo‘lgan massiv elementlarining o‘rta arifmetigi topilsin.'''
n = int(input("element sonini kiriting:"))
s=int(input("1-tanlangan indexsini kiriting:"))
S=int(input("2-tanlangan indexsinini kiriting:"))
a=[k for k in range(n,0,-1)]
b=[a[i] for i in range(s,S+1)]
print(sum(b)/(S-s+1))