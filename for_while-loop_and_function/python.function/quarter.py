def Quarter(x,y):
    if x<0 and y<0:
        return 3
    elif x<0 and y>0:
        return 2
    elif x>0 and y>0:
        return 1
    elif x>0 and y<0:
        return 4
    else:
        return "Noto\'g\'ri kiritdingiz sonlarni"
x=float(input('Haqiqiy son kiriting (x!=0):'))
y=float(input('2-Haqiqiy son kiriting(y!=0):'))
print(Quarter(x,y))