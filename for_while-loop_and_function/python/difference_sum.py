'''n(n>0) butun soni berilgan. 1,1-1,2+1,3-… Ifodaning qiymati topilsin. Shart operatori
qo‘llanilmasin.
2 -0.1'''
n=int(input('Son kiriting:'))
sum=0
for i in range(1,n+1):
    sum*=(-1)**(i+1)*(1+i/10)
print(sum)