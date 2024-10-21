'''е (е>0) haqiqiy son berilgan. ak haqiqiy sonlar ketma-ketligi quyidagicha aniqlanadi. a1=2
1
1
2

 
k
k
a
a
 k=2,3,…
│ak-ak-1│<е tengsizlikni qanoatlantiradigan birinchi k soni topilsin hamda k, ak-1 va ak chiqarilsin.
0.7 2 2 2.5'''
e=float(input('Butun son kiriting: '))
a1=2
k=1
ak=0
while a1-ak>e:
    ak=2+1/a1
    k+=1
    if a1-ak<e:
        break
    a1=2+1/ak
    k+=1
print(k,a1,ak)