a=int(input("Enter three room different number a="))
b=a%10
c=(a%100-b)/10
d=a//1000
e=a//100-d*10
print(b==d and c==e)
