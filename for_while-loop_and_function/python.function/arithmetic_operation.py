'''Nol bo‘lmagan haqiqiy a va b sonlari ustida 1 ta arifmetik amal bajaruvchi haqiqiy tipli
Calc(a,b,op) funksiyasi tasvirlansin. Bu yerda op parametri 1 bo‘lsa “ayirish”, 2 bo‘lsa
“ko‘paytirish”, 3 bo‘lsa “bo‘lish’, boshqa hollarda “qo‘shish” amaliga ekvivalent hisoblanadi. Bu
funksiy'''
def Calc(a,b,op):
    if op=='1':
        return a-b
    elif op=='2':
        return a*b
    elif op=='3':
        return a/b
    elif op=='4':
        return a+b
    else:
        return 'Bunday amal yo\'q'
a=int(input('Haqiqiy son kiriting:'))
b=int(input('2-Haqiqiy son kiriting:'))
op=input('amal kiriting((1)-,(2)*,(3)/,(4)+) kiriting:')
print(Calc(a,b,op))