'''Hech bo‘lmaganda 1 ta bo‘sh joyga ega satr berilgan. Berilgan satrdagi 1- va oxirgi bo‘sh
joylar orasida joylashgan qism satr chiqarilsin. Agar satr bo‘sh bo`lsa, bo‘sh satr chop etilsin.'''
s=input('Matin kiriting: ')
S=''
c=0
d=s.count(' ')
if ' ' in s:
    for i in s:
        if i==' ':
            c+=1
        if c>0:
            S+=i
        if c==d:
            break
print(S)