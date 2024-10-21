'''n(n>0) butun soni berilgan. Quyidagi formuladan foydalanib berilgan sonning kvadrati
hisoblansin: n
2=1+3+5+…+(2n-1). Har bir qadamdagi yig‘indi chiqarilsin(natijada 1 dan n gacha
bo‘lgan butun sonlarning kvadrati chiqadi).
4 1 4 9 16'''
n=int(input('Son kiriting:'))
sum=0
for i in range(1,n+1):
    sum+=(2*i-1)
    print(sum,end=' ')