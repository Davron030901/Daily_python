import math
x1=int(input("x1="))
x2=int(input("x2="))
x3=int(input("x3="))
y1=int(input("y1="))
y2=int(input("y2="))
y3=int(input("y3="))
l1=pow((pow(abs(x1-x2),2)+pow(abs(y1-y2),2)),0.5)
l2=pow((pow(abs(x3-x2),2)+pow(abs(y3-y2),2)),0.5)
l3=pow((pow(abs(x1-x3),2)+pow(abs(y1-y3),2)),0.5)
P=l1+l2+l3
p=P/2
S=pow((p*(p-l1)*(p-l2)*(p-l3)),0.5)
print("P=",P)
print("S=",S)