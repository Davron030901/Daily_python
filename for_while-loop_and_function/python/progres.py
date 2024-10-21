"""2. a va b butun sonlar berilgan(a>b). a va b sonlari orasidagi sonlarni o‘sish tartibida chiqarilsin(a
va b sonlari ham kiradi) hamda shu sonlar miqdori (soni) n chiqarilsin.
5 2---2 3 4 5 4"""
a=int(input('Son kiriting:'))
b=int(input('Kichik sonini kiriting:'))
count=0
for i in range(b,a+1):
    print(i,end=' ')
    count+=1
print(count)