'''s va s0 satrlar berilgan. s satrdan s0 satr bilan ustma-ust tushuvchi oxirgi qism satr o‘chirilsin.
Agar s satrda s0 satr topilmasa s satr o‘zgarishsiz chop etilsin. '''
s=input('Matin kiriting: ')
s0=input('Keyingi Matin kiriting: ')
s=s[::-1]
s0=s0[::-1]
if s0 in s:
    s=s.replace(s0,'',1)
print(s[::-1])