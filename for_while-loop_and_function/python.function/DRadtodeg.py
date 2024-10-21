'''Agar burchak o‘lchovi radianda berilgan bo‘lsa uni gradusda ifodalovchi haqiqiy tipli
DRadtodeg(r) funksiyasi tasvirlansin(r haqiqiy son 0<r<2р). Radianlarda berilgan 4 ta burchak
o‘lchovlarining har biri uchun gradus qiymatlari aniqlansin.
0 1.57 6.28 3.14 0 90 360 180'''
import math
def DRadtodeg(d):
    return math.ceil(d*180/math.pi)
for i in range(10):
    print(DRadtodeg(float(input('Radian o\'lchovini kiriting kiriting:'))))