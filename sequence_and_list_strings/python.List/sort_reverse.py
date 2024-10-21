''' n o‘lchamli butun sonli massiv berilgan. Massivdagi juft sonli elementlarining indekslarini
o‘sish tartibida, toq sonli elementlarining indekslarini kamayish tartibida tartiblab, massiv chop
etilsin.
6
7 4 7 3 5 10
2 6
5 4 3 1'''
n=int(input("list element sonini kiriting:"))
l=[i for i in range(n,1,-1)]
h=[]
s=[]
for j in range(0,len(l),2):
    h.append(l[j])
for i in range(1,len(l),2):
    s.append(l[i])
h.sort()
s.sort(reverse=True)
print(h,s)