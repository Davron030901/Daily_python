'''n(n>1) butun son berilgan. 1+2+…+k yig‘indining n dan katta yoki teng bo‘lishini
ta`minlaydigan eng kichik k butun soni va yig‘indining qiymati chiqarilsin. (1+2+…+k≥n)
10 4 10'''
n=int(input('son kiriting:'))
k=0
count=0
while count<n:
    k+=1
    count+=k
print(k,' ',count)