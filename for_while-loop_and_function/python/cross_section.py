a=float(input('Son kiriting:'))
b=float(input('Kattaroq son kiriting:'))
n=int(input('kesmani nechiga bo\'linishini kiriting:'))
sum=(b-a)/n
print(sum,'kesmadan, ')
for i in range(n+1):
    print(a,end=' ')
    a+=sum