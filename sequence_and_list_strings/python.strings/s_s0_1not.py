'''. s va s0 satrlar berilgan. s satrdan s0 satr bilan ustma-ust tushuvchi 1-qism satr o‘chirilsin. Agar
s satrda s0 satr topilmasa s satr o‘zgarishsiz chop etilsin. '''
s=input('Matin kiriting: ')
s0=input('Keyingi Matin kiriting: ')
if s0 in s:
    s=s.replace(s0,'',1)
print(s)