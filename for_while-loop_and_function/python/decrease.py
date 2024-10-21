"""3. a va b butun sonlar berilgan(a<b). a va b sonlari orasidagi sonlarni kamayish tartibida
chiqarilsin(a va b sonlari ham kiradi) hamda shu sonlar miqdori (soni) n chiqarilsin.
3 7 7 6 5 4 4"""
a=int(input('Son kiriting:'))
b=int(input('Kattaroq son kiriting:'))
count=0
for i in range(b,a-1,-1):
    print(i,end=' ')
    count+=1
print('   ',count,'ta son')