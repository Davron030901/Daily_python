'''n butun son va sonlar o‘qida 2 ta a, b (a<b) haqiqiy nuqtalar berilgan. [a,b] kesma n ta
teng kesmachalarga ajratilgan. Har bir kesma uzunligi h ni hamda [a,b] kesmani bo‘luvchi
nuqtalardagi f(x)=1-sin(x) funksiyaning qiymati chiqarilsin.
2 0.0 2.0 1.0 1.0 0.1 0.09 '''
import math
n=int(input('kesmani nechiga bo\'linishini kiriting:'))
a=float(input('Son kiriting:'))
b=float(input('Kattaroq son kiriting:'))
sum=(b-a)/n
print(sum,'kesmadan, ')
for i in range(n+1):
    print(1-math.sin(a),end=' ')
    a+=sum