'''a(a>1) son berilgan.
k
1
...
2
1
1  
yig‘indining a dan katta bo‘lishini ta`minlaydigan eng
kichik k butun son va yig‘indining qiymati chiqarilsin.






    a
k
1
...
2
1
1
1.5 3 1.8'''
a=float(input('son kiriting:'))
k=0
count=0
while count<=a:
    k+=1
    count+=1/k
print(k,' ',count)