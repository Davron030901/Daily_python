'''Agar burchak o‘lchovi gradusda berilgan bo‘lsa uni radianda ifodalovchi haqiqiy tipli
DegToRad(d) funksiyasi tasvirlansin(d haqiqiy son 0<d<360). Graduslarda berilgan 4 ta burchak
o‘lchovlarining har biri uchun radian qiymatlari aniqlansin.
0 90 360 180 ---0 1.57 6.28 3.14'''
import math
def DegToRad(d):
    return d*math.pi/180
for i in range(10):
    print(DegToRad(int(input('Burchakni kiriting:'))))