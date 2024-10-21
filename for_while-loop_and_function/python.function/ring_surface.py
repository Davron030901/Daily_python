'''2 ta r1, r2 (r1>r2) radiusli markazlari umumiy aylanalar bilan chegaralangan xalqa yuzasini
hisoblovchi haqiqiy tipli RingS(r1, r2) funksiyasi tasvirlansin(r1 va r2 haqiqiy). Bu funksiyadan
foydalanib ichki va tashqi radiuslari berilgan 3 ta xalqaning har biri uchun yuzalar hisoblansin.
4 2--37.68
2 1--9.42
3 2--15.7'''
import math
def RingS(r1,r2):
    S1=math.pi*r1**2
    S2=math.pi*r2**2
    return abs(S1-S2)
print(RingS(float(input('1-doira radiusini kiriting:')),float(input('2-doira radiusini kiriting:'))))