'''n(n>1) butun son berilgan. 1+2+…+k yig‘indining n dan kichik yoki teng bo‘lishini
ta’minlaydigan eng katta k butun son va yig‘indining qiymati chiqarilsin. (1+2+…+k≤n)
9 3 6'''
n=int(input('son kiriting:'))
k=0
count=0
while count<n-k:
    k+=1
    count+=k
print(k,' ',count)