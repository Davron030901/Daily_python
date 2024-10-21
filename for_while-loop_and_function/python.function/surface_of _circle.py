'''r radiusli doiraning yuzasini hisoblovchi haqiqiy tipli CircleS(r) funksiya tasvirlansin. Bu
funksiyadan foydalanib radiuslari berilgan 3 ta doiraning har birining yuzasi hisoblansin.
10 100 1 ---314 31400 3.14'''
import math
def CircleS(r):
    S=math.pi*r**2
    return S
print(CircleS(float(input('1-doira radiusini kiriting:'))),CircleS(float(input('2-doira radiusini kiriting:'))),CircleS(float(input('3-doira radiusini kiriting:'))))