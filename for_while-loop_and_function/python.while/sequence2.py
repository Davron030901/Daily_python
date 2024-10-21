'''е (е>0) haqiqiy son berilgan. ak haqiqiy sonlar ketma-ketligi quyidagicha aniqlanadi. a1=1
a2=2
 
3
2  2 1

k k
k
a a
a

│ak-ak-1│<е tengsizlikni qanoatlantiradigan birinchi k soni topilsin hamda k, ak-1 va ak chiqarilsin.
0.4 3 2 1.7'''
e=float(input('Butun son kiriting: '))
a1=1
a2=2
k=2
while a2-a1>e:
    a1=(a1+2*a2)/3
    k+=1
    if a1-a2<e:
        break
    a2=(a2+2*a1)/3
    k+=1
print(k,a2,a1)