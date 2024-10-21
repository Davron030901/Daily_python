'''n o‘lchamli, butun sonli massiv berilgan. Berilgan massivdagi barcha toq sonlarni o‘z ichiga
oladigan elementlarni o‘sish tartibida tartiblab, chop etilsin hamda ularning miqdori k aniqlansin.
5
3 2 12 7 6
2 7
2'''
n=int(input("list element sonini kiriting:"))
l=[i for i in range(n,1,-1)]
h=[]
for j in range(1,len(l),2):
    h.append(l[j])
h.sort()
print(h,len(h))