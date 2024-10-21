'''[A; B] dagi barcha butun sonlar yig‘indisini hisoblovchi butun tipli Range(A, B) funksiya
tasvirlansin(a va b – butun ). Agar a>b bo‘lsa funksiya 0 qaytarsin. Bu funksiyadan foydalanib, a,
b, c sonlari berilganda [a, b] va [b,c] segmentlardagi butun sonlarning yig‘indilari hisoblansin.
3 8 5 33 0'''
def Range(a,b,c) :
    sum=0
    if a>b and b>c:
        for i in range(b,a+1):
            sum+=i
        for j in range(c,b):
            sum+=j
        return 1,sum
    elif a>b and b<c and a>=c:
        for i in range(b,a+1):
            sum+=i
        return 1,sum
    elif a>b and b<c and a<c:
        for i in range(b,a):
            sum+=i
        for j in range(a,c+1):
            sum+=j
        return 1,sum
    elif a<b and a<c and b>=c:
        for i in range(a,b+1):
            sum+=i
        return sum,0
    elif a<b and a>c:
        for i in range(a,b+1):
            sum+=i
        for j in range(c,a):
            sum+=j
        return sum,0
    elif a<b and b<c:
        for i in range(a,c+1):
            sum+=i
        return sum,0
    else:
        if a>c:
            for i in range(c,a+1):
                sum+=i
            return sum,0
        elif a==c:
            sum=c
            return sum,0
        else:
            for i in range(a,c+1):
                sum+=i
            return sum,0

a=int(input('Haqiqiy son kiriting:'))
b=int(input('2-Haqiqiy son kiriting:'))
c=int(input('3-Haqiqiy son kiriting:'))
print(Range(a,b,c) )