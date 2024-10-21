'''Hech bo‘lmaganda 1 ta bo‘sh joyga ega satr berilgan. Berilgan satrdagi 1- va 2- bo‘sh joylar
orasida joylashgan qism satr chiqarilsin. Agar satr bo‘sh joy topilsa, bo‘sh satr chop etilsin. '''
s=input('Matin kiriting: ')
S=''
count=0
if ' ' in s:
    for i in s:
        if i==' ':
            count+=1
        if count==1:
            S+=i
        if count==2:
            break
print(S)