'''n o‘lchamli a massiv berilgan. Avval toq indeksdagi elementlar, keyin juft indeksdagi
elementlar kamayish tartibida chop etilsin.
6
1 2 3 4 5 6
5 3 1
6 4 2'''
n = int(input("element sonini kiriting:"))
a=[k for k in range(1,n)]
b=[a[i] for i in range(1,len(a),2)]
b.reverse()
print(b)
c=[a[i] for i in range(0,len(a),2)]
c.reverse()
print(c)