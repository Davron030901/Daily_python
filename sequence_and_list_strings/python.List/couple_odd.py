'''n o‘lchamli a massiv berilgan. Avval massivning juft indeksli elementlari(indekslarini o‘sish
tartibida) keyin toq indeksli elementlari (indekslarini o‘sish tartibida) chiqarilsin: a2, a4, a6, … a1,
a3, a5… Shart operatoridan foydalanilmasin.
6
5 4 3 2 1 0
4 2 0
5 3 1'''
n = int(input("element sonini kiriting:"))
a=[k for k in range(n,-1,-1)]
print([a[i] for i in range(1,len(a),2)])
print([a[i] for i in range(0,len(a),2)])
