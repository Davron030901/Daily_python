'''n(n>0) butun soni berilgan
n
1
...
2
1
1  
(Yig‘indi haqiqiy son). Yig‘indi hisoblansin.
2 1.5'''
a=int(input('Son kiriting:'))
sum=0
for i in range(1,a+1):
    sum+=(i**(-1))
print(sum)