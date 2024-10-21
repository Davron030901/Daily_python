'''. n butun soni berilgan n
3+(n+1)3+(n+2)3…+(2n)3
. (Yig‘indi butun son). Yig‘indi hisoblansin.
2 99'''
n=int(input('Son kiriting:'))

sum=0
for i in range(n+1):
    sum+=(n+i)**3
print(sum)