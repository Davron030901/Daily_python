'''fk Fibonachchi sonlarining n-hadini hisoblaydigan butun tipli Fib(n) funksiyasi tasvirlansin.
Bu funksiyadan foydalanib n1, n2, …, n5 nomerlarga to‘g‘ri keluvchi Fibonachchi sonlari topilsin.
6 2 3 4 5---- 8 1 2 3 5'''
def Fact2(n):
    f1=1
    f2=1
    for i in range(3,n+1,2):
        f1=f1+f2
        if n%2!=0 and i==n:
            break 
        f2=f2+f1
    if n%2!=0:
        return f1
    else:
        return f2
for i in range(5):
    print(Fact2(int(input('Burchakni kiriting:'))))